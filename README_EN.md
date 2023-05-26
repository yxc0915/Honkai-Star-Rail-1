<div align="center">

[Hi! Click me! Click me! Click me!](#instructions)

[Simplified Chinese](README.md) | [Traditional Chinese](README_CHT.md)| [English](README_EN.md) | [Documentation](https://sra.cyber-cn.top/)
 
<img alt="LOGO" src="../../blob/map/temp/love!.png" style="border-radius:50%">

<h1 align="center">

Honkai Star Rail Assistant

</h1>
 
[![GitHub Stars](https://img.shields.io/github/stars/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/network)
[![GitHub Issues](https://img.shields.io/github/issues/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/graphs/contributors)
[![GitHub License](https://img.shields.io/github/license/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/blob/main/LICENSE)
</div>

*****This script is still in the testing phase and may experience weird bugs*****
*** Collision with the wall when search the route? Are you not satisfied with the route? Now the map recording function has been added in the beta-2.7 version.***<br>
*** You can now use record_v7.2.py under the tool directory to record map paths, pack you to a satisfactory X D***

Found a bug? Want to criticize the code? Welcome to join the technical & chat group: [QQ Group](https://qm.qq.com/cgi-bin/qm/qr?k=xdCO46fHlVcY7D2L7elXzqcxL3nyTGnW&jump_from=webapi&authKey=uWZooQ2szv+nG/re7luCKn8LW1KibSb0vvi0FycA45Mglm5AGM1GP2iJ+SiWmDwg)|[Telegram Group](https://t.me/+yeQEhnuT9O41NDM1)<br>

~~This script currently only supports scaling 150%, screen resolution 2560x1440, and is now undergoing major changes in order to solve the screen rotation adaptation problem as soon as possible~~

## Disclaimer
This software is an external tool aimed at automating the gameplay of Honkai Star Rail. It is designed to interact with and respect the relevant laws and regulations only through existing user interfaces with games. The software package is designed to provide simplification and user interaction with games through functions, and it is not intended to disrupt the game balance in any way or provide any unfair advantages. The software package will not modify any game files or game code in any way.

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

Please note that according to "Honkai: there are no free lunches in the Star Rail game" by MiHoYo:

    "The use of third-party tools such as plug-ins, accelerators, and scripts that destroy game fairness is strictly prohibited."
    "Once discovered, miHoYo (hereinafter referred to as "us") will take measures such as deducting illegal income, freezing game accounts, and permanently banning game accounts based on the severity of the violation and the number of violations."

## Instructions

1: Install [Python 3.11](https://www.microsoft.com/store/productId/9NRWMJP3717K) (There will be many problems installing dependencies with other versions of Python)

1.1: Input `pip install -r requirements.txt` to install dependencies

2: Confirm that the game language is **Simplified Chinese**, the button configuration is all default, and the sensitivity is all default values

3: If your computer resolution is 2560\*1440, please adjust the game resolution to 1920\*1080 (windowed);<br>
   If your computer resolution is 1920\*1080, please set the game resolution to 1920\*1080 (full screen)

4: The battle is the game's own automatic battle. Make sure your team is strong enough to push small monsters normally<br>
   (If you have enabled the automatic battle persistence, please change "auto_battle_persistence" in config.json to 1)

5: It is recommended not to track anything on the map, and the character's initial position is preferably **observation car**

6: Please use **"ranged attack"** characters to open monsters, currently recommended **"March Seven"**, which has a more stable running effect.

7: Open **Honkai_Star_Rail.bat** and wait for the program to run to the input **map number**

8: If you don't know what **map number** to use or would like to start the map from the **beginning**, input "0" and press Enter.

9: During the five seconds before the start, click back into the game screen, ensure that no menus or interfaces are open, and wait for the program to run.

10: Do not move your keyboard or mouse during the program's runtime, as doing so may cause **deviation** or **wall collisions**.

## Configuration File Explanation
```json
{
    "real_width": 0, (actual width)
    "auto_battle_persistence": 0, (whether to enable auto-battle in-game, 1 to enable)
    "real_height": 0, (actual length)
    "map_debug": false, (whether to check for updates)
    "github_proxy": "", (github proxy)
    "rawgithub_proxy": "", (github proxy)
    "webhook_url": "",
    "start": true, (whether it's the first time running the script)
    "temp_version": "20230515205738",
    "star_version": "20230515220742",
    "open_map": "m", (open map button)
    "map_version": "20230515205738",
    "script_debug": true (whether to check for script updates)
}
```

## Script Recording - Thank you [@AlisaCat](https://github.com/AlisaCat-S)

1: Use WASD to move, X to enter combat, left-click to remove obstacles, F to interact, and do not move the mouse to look around (use the left and right arrow keys instead to look around, which will be mapped to mouse movement after the script runs). Only press one effective key at a time during the recording (multiple keys cannot be pressed simultaneously). The script will only record the duration of key presses and movement of the perspective, not any pauses in between. Record slowly and accurately. Press F9 to stop recording and save.

2: After completion, an output (time).json file will be generated. Rename it to the desired map json and save the screenshot of the teleportation point and rename it to temp to use (you can submit this to the map branch or give it to the administrator to submit).

3: Blank fields in the map json:
```json
{
    "name": "Ula-Ula-1",       (the map json is named 1-1_1.json)
    "author": "Starry-Wind",   (author name; second author doesn't overwrite the first author's name)
    "start": [           (set the initial teleportation point, identify the image, move the mouse to the center of the image, and press the key)
        {"map": 1},         (press m to open the map)
        {"temp\\orientation_1.jpg": 1.5},     (identify the orientation_1.jpg image, move the mouse to the center of the image, and press the key)
        {"temp\\map_1.jpg": 2},               (view the area name "Ula-Ula" on the map)
        {"temp\\map_1_point_1.jpg": 1.5},       (screenshot of the first teleportation point)
        {"temp\\transfer.jpg": 1.5}              (screenshot of the word "Transfer")
    ]
}
```

## Notes

1: Image recognition captures the game screen, so there can be no overlaps.

2: Supported maps include **Space Station "Black Tower," Yalilolu VI, and Xianzhou "Luo-Fu"**.

3: If you encounter any wall collision issues, you can help update the [map file here](https://github.com/Starry-Wind/StarRailAssistant/tree/map).

4: Please use **March 7** to run the map for the best experience.

⭐**Don't forget to give us a star~**⭐

## Future Goals

1: Simulation of the universe is currently under development.

2: GUI development.

3: Future updates will include searching for treasure boxes, playing Minecraft while picking up garbage, and other features.

## Contributors

Many thanks to the following contributors for their contributions to this project:

<a href="https://github.com/Starry-Wind/StarRailAssistant/graphs/contributors">

  <img src="https://contrib.rocks/image?repo=Starry-Wind/StarRailAssistant" />

</a>

![Alt](https://repobeats.axiom.co/api/embed/79d87540c597fc0b30893860e7b92da60c555fa9.svg "Repobeats analytics image")

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Starry-Wind/Honkai-Star-Rail&type=Date)](https://star-history.com/#Starry-Wind/Honkai-Star-Rail&Date)
