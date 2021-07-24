# LogoSkip: Automatically skip commercials on YouTube TV by looking for a logo

LogoSkip is a tool for automatically skipping commercials. It is intended to be used with YouTube TV, ans specifically with NBC's coverage of the 2020 Tokyo Olympic Games.

Most NBC channels on YouTube TV identify non-commercial content by including the olympic rings logo. This tool looks for that logo, and skips ahead when it goes away, until it comes back.

This script uses [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/) to monitor your screen for the approximate presence of the logo image. If it doens't see the logo for long enough, it uses YouTube TV keyboard commands to pause the video (`k`) and skip ahead (`l`) until the logo reappears.

## Disclaimer

Using this script might be against the YouTube TV terms of service. I didn't read them and neither, presumably, did you. When Google deletes you from the Internet, it is 100% their fault, not mine. Not a lawyer, do your own crimes, &c.

## Installation

Clone the repository and install dependencies:

```
git clone https://github.com/interfect/logoskip
cd logoskip
virtualenv --python python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

You may also need the `scrot` tool on Ubuntu:

```
sudo apt-get install scrot
```

## Usage

1. Make sure you are running in 1920 x 1080 resolution (1080p). If not, change your screen resolution, or replace the included `rings.png` with a cropped screenshot of the olympic rings logo as it appears when the broadcast is fullscreened on your system.

2. Open the content you want to watch in full screen on Youtube TV, and start it playing.

3. In a terminal window, run `./logoskip.py`.

4. Quickly change back to the full screen YouTube TV browser window, and make sure it has focus.

5. Watch your content. When the logo vanishes, the script will generate a series of keypresses to control the player and (hopefully) skip the commercials.

6. To stop the script, switch to the terminal window it is running in and `ctrl+c` it.

## Known issues

1. Can't work with Wayland, because `scrot`, which PyAutoGui uses, doesn't work with Wayland. See [here](https://github.com/asweigart/pyautogui/issues/280) and maybe [also here](https://github.com/asweigart/pyautogui/issues/556).


