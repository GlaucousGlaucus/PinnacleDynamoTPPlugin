import sys
import requests
import TouchPortalAPI as tp
from TouchPortalAPI.logger import Logger
from requests import Response

from constants import (
    PLUGIN_ID,
    __version__,
    PluginActionIDs,
    PluginActionDataIDs,
)
from entry_tp_gen import (
    TP_PLUGIN_SETTINGS, # noqa: F401
    TP_PLUGIN_INFO, # noqa: F401
    TP_PLUGIN_CATEGORIES, # noqa: F401
    TP_PLUGIN_ACTIONS, # noqa: F401
    TP_PLUGIN_EVENTS, # noqa: F401
    TP_PLUGIN_STATES, # noqa: F401
)

try:
    TPClient = tp.Client(
        pluginId=PLUGIN_ID,
        sleepPeriod=0.05,
        autoClose=True,
        checkPluginId=True,
        maxWorkers=4,
        updateStatesOnBroadcast=False,
    )
except Exception as e:
    sys.exit(f"Could not create TP Client: {repr(e)}")

g_log = Logger(name=PLUGIN_ID)


def _flatten_settings(settings):
    return {list(item.keys())[0]: list(item.values())[0] for item in settings}


def handleSettings(settings, on_connect=False):
    flat = _flatten_settings(settings)
    for settings_id, settings_data in TP_PLUGIN_SETTINGS.items():
        name = settings_data.get("name")
        if name in flat:
            TP_PLUGIN_SETTINGS[settings_id]["value"] = flat[name]
    g_log.info("Settings updated")


@TPClient.on(tp.TYPES.onConnect)
def onConnect(data):
    g_log.info(
        f"Connected to TP v{data.get('tpVersionString', '?')}, "
        f"plugin v{data.get('pluginVersion', '?')}."
    )
    if data.get("settings"):
        handleSettings(data["settings"], True)


@TPClient.on(tp.TYPES.onSettingUpdate)
def onSettingUpdate(data):
    if data.get("values"):
        handleSettings(data["values"], False)


def _base_address():
    return (
        f"http://{TP_PLUGIN_SETTINGS['api_address']['value']}:"
        f"{TP_PLUGIN_SETTINGS['api_port']['value']}"
    )


def _post(path):
    address = f"{_base_address()}{path}"
    response: Response = requests.post(address)
    g_log.info(f"PD API Response: {response.text} for {address}")


def _delete(path):
    address = f"{_base_address()}{path}"
    response: Response = requests.delete(address)
    g_log.info(f"PD API Response: {response.text} for {address}")


@TPClient.on(tp.TYPES.onAction)
def onAction(data):
    aid = data.get("actionId")
    if not aid:
        return

    if aid == PluginActionIDs.TRIGGER_NEXT_SLIDE:
        _post("/presentation/active/next/trigger")
    elif aid == PluginActionIDs.TRIGGER_PREV_SLIDE:
        _post("/presentation/active/prev/trigger")
    elif aid == PluginActionIDs.TRIGGER_NEXT_PRESENTATION:
        _post("/presentation/next/trigger")
    elif aid == PluginActionIDs.TRIGGER_PREV_PRESENTATION:
        _post("/presentation/prev/trigger")
    elif aid == PluginActionIDs.CLEAR_LAYER:
        layer = TPClient.getActionDataValue(
            data.get("data"), PluginActionDataIDs.LAYER_PICKER
        )
        _delete(f"/clear/layer/{layer}")
    elif aid == PluginActionIDs.CLEAR_ALL_LAYERS:
        _delete("/clear/layer/all")
    else:
        g_log.warning(f"Unknown action ID: {aid}")


@TPClient.on(tp.TYPES.onShutdown)
def onShutdown(data):
    g_log.info("Received shutdown event from TP Client.")


@TPClient.on(tp.TYPES.onError)
def onError(exc):
    g_log.error(f"TP Client error: {repr(exc)}")


def main():
    log_file = f"./{PLUGIN_ID}.log"
    log_stream = sys.stdout

    TPClient.setLogFile(log_file)
    TPClient.setLogStream(log_stream)
    TPClient.setLogLevel("DEBUG")

    g_log.info(
        f"Starting {TP_PLUGIN_INFO['name']} v{__version__} on {sys.platform}."
    )

    ret = 0
    try:
        TPClient.connect()
    except KeyboardInterrupt:
        g_log.warning("Keyboard interrupt, exiting.")
    except Exception:
        from traceback import format_exc

        g_log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        TPClient.disconnect()

    g_log.info(f"{TP_PLUGIN_INFO['name']} stopped.")
    return ret


if __name__ == "__main__":
    sys.exit(main())
