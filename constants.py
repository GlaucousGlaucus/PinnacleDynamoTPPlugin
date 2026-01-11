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

    MEDIA_NEXT_ITEM = f"{PLUGIN_ID}.act.media-next-item"
    MEDIA_PREV_ITEM = f"{PLUGIN_ID}.act.media-prev-item"
    MEDIA_SELECT_ITEM = f"{PLUGIN_ID}.act.media-select-item"

    MEDIA_NEXT_PLAYLIST = f"{PLUGIN_ID}.act.media-next-playlist"
    MEDIA_PREV_PLAYLIST = f"{PLUGIN_ID}.act.media-prev-playlist"
    MEDIA_SELECT_PLAYLIST = f"{PLUGIN_ID}.act.media-select-playlist"

    MEDIA_SET_FROM_PATH = f"{PLUGIN_ID}.act.media-set-from-path"


class PluginActionDataIDs:
    LAYER_PICKER = f"{PluginActionIDs.CLEAR_LAYER}.data.layer-picker"

    STAGE_MESSAGE_TEXT = f"{PluginActionIDs.SET_STAGE_MESSAGE}.data.message-text"
    STAGE_LAYOUT_PICKER = f"{PluginActionIDs.SET_STAGE_LAYOUT}.data.layout-picker"

    MEDIA_ITEM_ID = f"{PluginActionIDs.MEDIA_SELECT_ITEM}.data.item-id"
    MEDIA_PLAYLIST_ID = f"{PluginActionIDs.MEDIA_SELECT_PLAYLIST}.data.playlist-id"

    MEDIA_LAYER_SELECT_ITEM = f"{PluginActionIDs.MEDIA_SELECT_ITEM}.data.layer"
    MEDIA_LAYER_FROM_PATH = f"{PluginActionIDs.MEDIA_SET_FROM_PATH}.data.layer"

    MEDIA_ABSOLUTE_PATH = f"{PluginActionIDs.MEDIA_SET_FROM_PATH}.data.path"
