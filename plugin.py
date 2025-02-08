import sys
from argparse import ArgumentParser

import TouchPortalAPI as TP
import requests
from TouchPortalAPI.logger import Logger
from requests import Response

from constants import PLUGIN_ID, __version__, PluginActionIDs, PluginActionDataIDs
from entry_tp_gen import TP_PLUGIN_SETTINGS, TP_PLUGIN_INFO, TP_PLUGIN_ACTIONS, TP_PLUGIN_STATES, TP_PLUGIN_CATEGORIES

# Create the Touch Portal API client.
try:
    TPClient = TP.Client(
        pluginId = PLUGIN_ID,  # required ID of this plugin
        sleepPeriod = 0.05,    # allow more time than default for other processes
        autoClose = True,      # automatically disconnect when TP sends "closePlugin" message
        checkPluginId = True,  # validate destination of messages sent to this plugin
        maxWorkers = 4,        # run up to 4 event handler threads
        updateStatesOnBroadcast = False,  # do not spam TP with state updates on every page change
    )
except Exception as e:
    sys.exit(f"Could not create TP Client, exiting. Error was:\n{repr(e)}")

g_log = Logger(name=PLUGIN_ID)

# Settings will be sent by TP upon initial connection to the plugin,
# as well as whenever they change at runtime. This example uses a
# shared function to handle both cases. See also onConnect() and onSettingUpdate()
def handleSettings(settings, on_connect=False):
    # the settings array from TP can just be flattened to a single dict,
    # from:
    #   [ {"Setting 1" : "value"}, {"Setting 2" : "value"} ]
    # to:
    #   { "Setting 1" : "value", "Setting 2" : "value" }
    settings = { list(settings[i])[0] : list(settings[i].values())[0] for i in range(len(settings)) }
    for settings_id, settings_data in TP_PLUGIN_SETTINGS.items():
        if (name := settings_data.get("name")) in settings:
            TP_PLUGIN_SETTINGS[settings_id]['value'] = settings.get(name)
    g_log.info("Settings Updated")

## TP Client event handler callbacks
# Initial connection handler
@TPClient.on(TP.TYPES.onConnect)
def onConnect(data):
    g_log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
    g_log.debug(f"Connection: {data}")
    if settings := data.get('settings'):
        handleSettings(settings, True)

# Settings handler
@TPClient.on(TP.TYPES.onSettingUpdate)
def onSettingUpdate(data):
    g_log.debug(f"Settings: {data}")
    if settings := data.get('values'):
        handleSettings(settings, False)

# Action handler
@TPClient.on(TP.TYPES.onAction)
def onAction(data):
    g_log.debug(f"Action: {data}")
    # check that `data` and `actionId` members exist and save them for later use
    if not (aid := data.get('actionId')):
    # if not (action_data := data.get('data')) or not (aid := data.get('actionId')):
            return
    base_address = f"{TP_PLUGIN_SETTINGS['api_address']['value']}:{TP_PLUGIN_SETTINGS['api_port']['value']}"
    if aid == PluginActionIDs.TRIGGER_NEXT_SLIDE:
        address = f"{base_address}/presentation/active/next/trigger"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    elif aid == PluginActionIDs.TRIGGER_PREV_SLIDE:
        address = f"{base_address}/presentation/active/prev/trigger"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    elif aid == PluginActionIDs.TRIGGER_NEXT_PRESENTATION:
        address = f"{base_address}/presentation/next/trigger"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    elif aid == PluginActionIDs.TRIGGER_PREV_PRESENTATION:
        address = f"{base_address}/presentation/prev/trigger"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    elif aid == PluginActionIDs.CLEAR_LAYER:
        layer = TPClient.getActionDataValue(data.get("data"), PluginActionDataIDs.LAYER_PICKER)
        address = f"{base_address}/clear/layer/{layer}"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    elif aid == PluginActionIDs.CLEAR_ALL_LAYERS:
        address = f"{base_address}/clear/layer/all"
        response: Response = requests.get(address)
        g_log.info(f"PD API Response: {response.text} for {address}")
    else:
        # set our example State text and color values with the data from this action
        # text = TPClient.getActionDataValue(action_data, TP_PLUGIN_ACTIONS['example']['data']['text'])
        # color = TPClient.getActionDataValue(action_data, TP_PLUGIN_ACTIONS['example']['data']['color'])
        # TPClient.stateUpdate(TP_PLUGIN_STATES['text']['id'], text)
        # TPClient.stateUpdate(TP_PLUGIN_STATES['color']['id'], color)
        g_log.warning("Got unknown action ID: " + aid)

# Shutdown handler
@TPClient.on(TP.TYPES.onShutdown)
def onShutdown(data):
    g_log.info('Received shutdown event from TP Client.')
    # We do not need to disconnect manually because we used `autoClose = True`
    # when constructing TPClient()
    # TPClient.disconnect()

# Error handler
@TPClient.on(TP.TYPES.onError)
def onError(exc):
    g_log.error(f'Error in TP Client event handler: {repr(exc)}')
    # ... do something ?

## main

def main():
    global TPClient, g_log
    ret = 0  # sys.exit() value

    # default log file destination
    logFile = f"./{PLUGIN_ID}.log"
    # default log stream destination
    logStream = sys.stdout

    # Set up and handle CLI arguments. These all relate to logging options.
    # The plugin can be run with "-h" option to show available argument options.
    # Addtionally, a file constaining any of these arguments can be specified on the command line
    # with the `@` prefix. For example: `plugin-example.py @config.txt`
    # The file must contain one valid argument per line, including the `-` or `--` prefixes.
    # See the plugin-example-conf.txt file for an example config file.
    # parser = ArgumentParser(fromfile_prefix_chars='@')
    # parser.add_argument("-d", action='store_true',
    #                     help="Use debug logging.")
    # parser.add_argument("-w", action='store_true',
    #                     help="Only log warnings and errors.")
    # parser.add_argument("-q", action='store_true',
    #                     help="Disable all logging (quiet).")
    # parser.add_argument("-l", metavar="<logfile>",
    #                     help=f"Log file name (default is '{logFile}'). Use 'none' to disable file logging.")
    # parser.add_argument("-s", metavar="<stream>",
    #                     help="Log to output stream: 'stdout' (default), 'stderr', or 'none'.")

    # # his processes the actual command line and populates the `opts` dict.
    # opts = parser.parse_args()
    # del parser
    #
    # # trim option string (they may contain spaces if read from config file)
    # opts.l = opts.l.strip() if opts.l else 'none'
    # opts.s = opts.s.strip().lower() if opts.s else 'stdout'
    # print(opts)
    #
    # # Set minimum logging level based on passed arguments
    # logLevel = "INFO"
    # if opts.q: logLevel = None
    # elif opts.d: logLevel = "DEBUG"
    # elif opts.w: logLevel = "WARNING"
    #
    # # set log file if -l argument was passed
    # if opts.l:
    #     logFile = None if opts.l.lower() == "none" else opts.l
    # # set console logging if -s argument was passed
    # if opts.s:
    #     if opts.S == "stderr": logStream = sys.stderr
    #     elif opts.s == "stdout": logStream = sys.stdout
    #     else: logStream = None

    # Configure the Client logging based on command line arguments.
    # Since the Client uses the "root" logger by default,
    # this also sets all default logging options for any added child loggers, such as our g_log instance we created earlier.
    TPClient.setLogFile(logFile)
    TPClient.setLogStream(logStream)
    TPClient.setLogLevel("DEBUG")

    # ready to go
    g_log.info(f"Starting {TP_PLUGIN_INFO['name']} v{__version__} on {sys.platform}.")

    try:
        # Connect to Touch Portal desktop application.
        # If connection succeeds, this method will not return (blocks) until the client is disconnected.
        TPClient.connect()
        g_log.info('TP Client closed.')
    except KeyboardInterrupt:
        g_log.warning("Caught keyboard interrupt, exiting.")
    except Exception:
        # This will catch and report any critical exceptions in the base TPClient code,
        # _not_ exceptions in this plugin's event handlers (use onError(), above, for that).
        from traceback import format_exc
        g_log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        # Make sure TP Client is stopped, this will do nothing if it is already disconnected.
        TPClient.disconnect()

    # TP disconnected, clean up.
    del TPClient

    g_log.info(f"{TP_PLUGIN_INFO['name']} stopped.")
    return ret


if __name__ == "__main__":
    sys.exit(main())