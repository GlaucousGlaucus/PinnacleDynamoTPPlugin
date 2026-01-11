__version__ = 120
PLUGIN_ID = "pinnacle_dynamo"
PLUGIN_NAME = "Pinnacle Dynamo Integration"


class PluginCategories:
    PRESENTATION = f"{PLUGIN_ID}.cat.presentation"
    CLEAR = f"{PLUGIN_ID}.cat.clear"
    STAGE = f"{PLUGIN_ID}.cat.stage"


class PluginActionIDs:
    TRIGGER_NEXT_SLIDE = f"{PLUGIN_ID}.act.trigger-next-slide"
    TRIGGER_PREV_SLIDE = f"{PLUGIN_ID}.act.trigger-prev-slide"

    TRIGGER_NEXT_PRESENTATION = f"{PLUGIN_ID}.act.trigger-next-presentation"
    TRIGGER_PREV_PRESENTATION = f"{PLUGIN_ID}.act.trigger-prev-presentation"

    CLEAR_ALL_LAYERS = f"{PLUGIN_ID}.act.clear-all-layers"
    CLEAR_LAYER = f"{PLUGIN_ID}.act.clear-layer"

    GET_STAGE_MESSAGE = f"{PLUGIN_ID}.act.get-stage-message"
    SET_STAGE_MESSAGE = f"{PLUGIN_ID}.act.set-stage-message"
    CLEAR_STAGE_MESSAGE = f"{PLUGIN_ID}.act.clear-stage-message"

    SET_STAGE_LAYOUT = f"{PLUGIN_ID}.act.set-stage-layout"


class PluginActionDataIDs:
    LAYER_PICKER = f"{PluginActionIDs.CLEAR_LAYER}.data.layer-picker"

    STAGE_MESSAGE_TEXT = f"{PluginActionIDs.SET_STAGE_MESSAGE}.data.message-text"
    STAGE_LAYOUT_PICKER = f"{PluginActionIDs.SET_STAGE_LAYOUT}.data.layout-picker"
