# Before using, please ensure configuration file correctness.

# About example_config.json

## "src_dir"
The path where Chrome browser downloads files.

## "radiko_extension_path"
Downloads Rajiko.crx to the root directory of the Python file, changes the extension to .rar, and extracts it to a folder. Fill in the relative path of the folder here in "radiko_extension_path". If Rajiko plugin is not downloaded, the download cannot be completed.

## "mouse_positions"
If these four [x, y] coordinates change due to different screens (if you run this file on a different computer, these four coordinates will definitely change), you need to obtain them again. Use the get_mouse_xy.py file to obtain these four coordinates.

## "url_template"
If the broadcast schedule changes, the URL template string needs to be updated.

## "dst_dir"
After downloading the broadcast, organize it into a new folder and rename it as yyyymmdd radio_name.aac.

## Before running, rename example_config.json to config.json

# Remarks
1. It is not possible to download other broadcasts directly by adding a broadcast in config.json.
2. When using the Selenium library to load Chrome plugins with add_argument, the complete path of the extension must be used. Using a relative path will cause an error, seemingly due to an issue with the Selenium library.
3. Edge cannot be used because Rajiko may have bugs when running on Edge, which may result in the inability to download the correct AAC file, causing the program to fail to find the AAC file in "src_dir".
