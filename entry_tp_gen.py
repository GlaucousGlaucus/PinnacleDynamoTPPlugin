from build import PLUGIN_ROOT
from constants import PLUGIN_ID, PLUGIN_NAME, __version__, PluginActionIDs, PluginActionDataIDs, \
    PluginCategories

TP_PLUGIN_INFO = {
    'api': 10,
    'version': __version__,  # TP only recognizes integer version numbers
    'name': PLUGIN_NAME,
    'id': PLUGIN_ID,
    # Startup command, with default logging options read from configuration file (see main() for details)
    "plugin_start_cmd": f"%TP_PLUGIN_FOLDER%{PLUGIN_ROOT}\\pd_plugin.exe",
    'configuration': {
        'colorDark': "#25274c",
        'colorLight': "#707ab5"
    },
    "doc": {
        "Install": "example install instruction",
        "description": "example description"
    }
}

# Setting(s) for this plugin.
TP_PLUGIN_SETTINGS = {
    'api_address': {
        'name': "API IP",
        'type': "text",
        'default': r"127.0.0.1",
        'readOnly': False,  # this is also the default
        "doc": "The address for the API",
        'value': None  # we can optionally use the settings struct to hold the current value
    },
    'api_port': {
        'name': "API Port",
        'type': "number",
        'default': "5010",
        'readOnly': False,  # this is also the default
        "doc": "The Port to which the plugin will connect to. You can do in your software > Settings > Network"
               "and see the port from there",
        'value': None  # we can optionally use the settings struct to hold the current value
    },
}

TP_PLUGIN_CATEGORIES = {
    "main": {
        "category": "main",
        'id': PluginCategories.PRESENTATION,
        'name': "PinnacleDynamoPlugin",
        'imagepath': r"%TP_PLUGIN_FOLDER%PinnacleDynamoTouchPortalPlugin/Resources/images/o-1.png"
    },
}

ACTION_PREFIX = TP_PLUGIN_CATEGORIES["main"]["name"]

TP_PLUGIN_ACTIONS = {
    'trigger_next_slide': {
        # 'category' is optional, if omitted then this action will be added to all, or the only, category(ies)
        'category': "main",
        'id': PluginActionIDs.TRIGGER_NEXT_SLIDE,
        'name': "Trigger Next Slide",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Triggers the next slide in cue",
        # 'format' tokens like $[1] will be replaced in the generated JSON with the corresponding data id wrapped with "{$...$}".
        # Numeric token values correspond to the order in which the data items are listed here, while text tokens correspond
        # to the last part of a dotted data ID (the part after the last period; letters, numbers, and underscore allowed).
        'format': "Trigger next slide in cue",
        'data': {
        }
    },
    'trigger_prev_slide': {
        'category': "main",
        'id': PluginActionIDs.TRIGGER_PREV_SLIDE,
        'name': "Trigger Previous Slide",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Triggers the previous slide in cue",
        'format': "Trigger previous slide in cue",
        'data': {
        }
    },
    'trigger_next_presentation': {
        'category': "main",
        'id': PluginActionIDs.TRIGGER_NEXT_PRESENTATION,
        'name': "Trigger Next Presentation",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Triggers the next presentation",
        'format': "Trigger next presentation",
        'data': {
        }
    },
    'trigger_prev_presentation': {
        'category': "main",
        'id': PluginActionIDs.TRIGGER_PREV_PRESENTATION,
        'name': "Trigger Previous Presentation",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Triggers the previous presentation",
        'format': "Trigger previous presentation",
        'data': {
        }
    },
    'clear_all_layers': {
        'category': "main",
        'id': PluginActionIDs.CLEAR_ALL_LAYERS,
        'name': "Clear All Layers",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Clears all layers",
        'format': "Clear All Layers",
        'data': {
        }
    },
    'clear_layer': {
        'category': "main",
        'id': PluginActionIDs.CLEAR_LAYER,
        'name': "Clear Layer",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Clears the specified layer",
        'format': "Clear $[1] layer",
        'data': {
            "layers": {
                "id": PluginActionDataIDs.LAYER_PICKER,
                "type": "choice",
                "label": "Layer",
                "default": "",
                "valueChoices": [
                    "media",
                    "foreground",
                    "slide",
                    "audio"
                ]
            }
        }
    },
}

# Stage
TP_PLUGIN_ACTIONS.update({

    'get_stage_message': {
        'category': "main",
        'id': PluginActionIDs.GET_STAGE_MESSAGE,
        'name': "Get Stage Message",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Fetches the current stage message",
        'format': "Get stage message",
        'data': {}
    },

    'set_stage_message': {
        'category': "main",
        'id': PluginActionIDs.SET_STAGE_MESSAGE,
        'name': "Set Stage Message",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Sets the stage message",
        'format': "Set stage message: $[1]",
        'data': {
            "message": {
                "id": PluginActionDataIDs.STAGE_MESSAGE_TEXT,
                "type": "text",
                "label": "Stage Message",
                "default": ""
            }
        }
    },

    'clear_stage_message': {
        'category': "main",
        'id': PluginActionIDs.CLEAR_STAGE_MESSAGE,
        'name': "Clear Stage Message",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Clears the stage message",
        'format': "Clear stage message",
        'data': {}
    },

    'set_stage_layout': {
        'category': "main",
        'id': PluginActionIDs.SET_STAGE_LAYOUT,
        'name': "Set Stage Layout",
        'prefix': ACTION_PREFIX,
        'type': "communicate",
        'tryInline': True,
        "doc": "Sets the stage screen layout",
        'format': "Set stage layout to $[1]",
        'data': {
            "layout_type": {
                "id": PluginActionDataIDs.STAGE_LAYOUT_PICKER,
                "type": "choice",
                "label": "Layout",
                "default": "normal",
                "valueChoices": [
                    "normal",
                    "screen-capture",
                    "window-capture",
                    "audience-scene",
                    "slides-view"
                ]
            }
        }
    },

})

TP_PLUGIN_STATES = {
    # 'text': {
    #     # 'category' is optional, if omitted then this state will be added to all, or the only, category(ies)
    #     'category': "main",
    #     'id': PLUGIN_ID + ".state.text",
    #     # "text" is the default type and could be omitted here
    #     'type': "text",
    #     'desc': "Example State Text",
    #     # we can conveniently use a value here which we already defined above
    #     'default': TP_PLUGIN_ACTIONS['example']['data']['text']['default']
    # },
}

TP_PLUGIN_EVENTS = {}

