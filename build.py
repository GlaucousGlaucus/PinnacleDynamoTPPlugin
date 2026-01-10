from TouchPortalAPI import tppbuild
import constants

PLUGIN_MAIN = "plugin.py"
PLUGIN_EXE_NAME = "pd_plugin"
PLUGIN_EXE_ICON = r"Resources/images/pd_main.ico"

PLUGIN_ROOT = "PDPlugin"
OUTPUT_PATH = r"./dist"

PLUGIN_ENTRY = PLUGIN_MAIN
PLUGIN_ENTRY_INDENT = 2

PLUGIN_ICON = r""
PLUGIN_VERSION = constants.__version__

ADDITIONAL_FILES: list[str] = []

ADDITIONAL_PYINSTALLER_ARGS = [
    "--log-level=WARN",
]

if __name__ == "__main__":
    tppbuild.runBuild()
