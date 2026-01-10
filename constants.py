__version__ = "1.1"
PLUGIN_ID = "pinnacle_dynamo"
PLUGIN_NAME = "Pinnacle Dynamo Integration"

class PluginCategories:
    PRESENTATION = f"{PLUGIN_ID}.cat.presentation"
    CLEAR = f"{PLUGIN_ID}.cat.clear"

class PluginActionIDs:
    TRIGGER_NEXT_SLIDE = f"{PLUGIN_ID}.act.trigger-next-slide"
    TRIGGER_PREV_SLIDE = f"{PLUGIN_ID}.act.trigger-prev-slide"

    TRIGGER_NEXT_PRESENTATION = f"{PLUGIN_ID}.act.trigger-next-presentation"
    TRIGGER_PREV_PRESENTATION = f"{PLUGIN_ID}.act.trigger-prev-presentation"

    CLEAR_ALL_LAYERS = f"{PLUGIN_ID}.act.clear-all-layers"
    CLEAR_LAYER = f"{PLUGIN_ID}.act.clear-layer"

class PluginActionDataIDs:
    LAYER_PICKER = f"{PluginActionIDs.CLEAR_LAYER}.data.layer-picker"