# Pinnacle Dynamo Touch Portal Plugin

This is a touch portal plugin for controlling [Pinnacle Dynamo](https://github.com/GlaucousGlaucus/PinnacleDynamo) using its API.

# Installation

Download the [tpp file]() and import it into Touch Portal.

# Usage

All the commands will be listed in the plugin's category.


## Build Configuration (TouchPortal `tppbuild`)

This plugin uses `TouchPortalAPI.tppbuild` for packaging.

The build script is declarative and relies on specific module-level variables.
Only the variables listed below are read by `tppbuild`.

### Required Variables

| Variable | Description |
|--------|-------------|
| `PLUGIN_ROOT` | Root directory name inside the generated `.tpp` archive |
| `OUTPUT_PATH` | Output directory for the generated `.tpp` file |
| `PLUGIN_MAIN` | Path to the main Python plugin file |
| `PLUGIN_EXE_NAME` | Name of the compiled executable |
| `PLUGIN_ENTRY` | Path to `entry.tp` **or** a Python file defining the entry metadata |
| `PLUGIN_ENTRY_INDENT` | JSON indentation level for generated `entry.tp` |
| `PLUGIN_VERSION` | Version string used in the `.tpp` filename |

### Optional Variables

| Variable | Description |
|--------|-------------|
| `PLUGIN_EXE_ICON` | Path to `.ico` or `.png` icon for the executable |
| `PLUGIN_ICON` | Icon path used in `entry.tp` (`imagepath`) |
| `ADDITIONAL_FILES` | Extra files bundled into the plugin |
| `ADDITIONAL_PYINSTALLER_ARGS` | Extra arguments passed to PyInstaller |

### Notes

- Comments in the build script are ignored by `tppbuild`.
- Only variable names and values are evaluated.
- Validation of `entry.tp` is handled automatically by `tppbuild`.

### References

- TouchPortal API documentation
- `TouchPortalAPI.tppbuild` source code
