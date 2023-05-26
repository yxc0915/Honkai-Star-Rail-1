<div align="center">

[嗨！点点我！点点我！点点我！ ](#使用说明)

[简体中文](README.md) | [繁体中文](README_CHT.md) | [英文](README_EN.md)| [文档](https://sra.stysqy.top)
 
<img alt="LOGO" src="../../blob/map/temp/love!.png" style="border-radius:50%">

<h1 align="center">

崩坏：星穹铁道小助手|StarRailAssistant|StarRailAssistant

</h1>
 
[![GitHub Stars](https://img.shields.io/github/stars/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/network)
[![GitHub Issues](https://img.shields.io/github/issues/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/graphs/contributors)
[![GitHub License](https://img.shields.io/github/license/Starry-Wind/StarRailAssistant?style=flat-square)](https://github.com/Starry-Wind/StarRailAssistant/blob/main/LICENSE)
</div>

*****该脚本仍然处于测试阶段，可能会出现奇奇怪怪的BUG*****

***寻路撞墙？走的路径不对？嫌弃路线太慢？现在beta-2.7新增加地图录制功能***<br>
***你现在可以使用tool目录下的record_v7.2.py自行录制地图路径，包你走到满意 XD***

找到BUG了？代码问题想吐槽？欢迎加入 技术 & 吹水群：[QQ 群](https://qm.qq.com/cgi-bin/qm/qr?k=xdCO46fHlVcY7D2L7elXzqcxL3nyTGnW&jump_from=webapi&authKey=uWZooQ2szv+nG/re7luCKn8LW1KibSb0vvi0FycA45Mglm5AGM1GP2iJ+SiWmDwg)|[Telegram Group](https://t.me/+yeQEhnuT9O41NDM1)<br>

~~该脚本当前版本仅支持 缩放150%，屏幕分辨率2560x1440，现在在大改动中，尽快解决屏幕旋转适配问题~~

## 免责声明
本软件是一个外部工具旨在自动化崩坏星轨的游戏玩法。它被设计成仅通过现有用户界面与游戏交互,并遵守相关法律法规。该软件包旨在提供简化和用户通过功能与游戏交互,并且它不打算以任何方式破坏游戏平衡或提供任何不公平的优势。该软件包不会以任何方式修改任何游戏文件或游戏代码。

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。


请注意，根据MiHoYo的 [崩坏:星穹铁道的公平游戏宣言](https://sr.mihoyo.com/news/111246?nav=news&type=notice):

    "严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
    "一经发现，米哈游（下亦称“我们”）将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"

## 使用说明

1：安装[Python 3.11](https://www.microsoft.com/store/productId/9NRWMJP3717K) (其他版本安装依赖项时会有很多问题)

1.1: 输入`pip install -r requirements.txt`安装依赖

2：确认游戏语言为**简体中文**，按键配置皆为默认，灵敏度皆为默认值

3：如果你的电脑分辨率为2560\*1440，请将游戏分辨率调为1920\*1080（窗口化）<br>
   如果你的电脑分辨率为1920\*1080，请将游戏分辨率调为1920\*1080（全屏幕）
   
4：战斗为游戏自带的自动战斗，确保你的队伍有足够实力平推小怪<br>
   (如启用了沿用自动战斗设定，请把config.json里的 "auto_battle_persistence" 改成 1) 

5：建议不要在地图上追踪任何东西，并且人物初始位置最好在**观景车厢**

6：开怪角色请使用**远程攻击**角色，目前推荐**三月七**，跑图效果较稳定

7：开启**Honkai_Star_Rail.bat**等待程序自动运行至可输入**地图编号**处

8：如果你不知道**地图编号**是什么，或是你想要**重头开始**跑图，输入"0"后回车

9：在等待开始五秒期间，请点回游戏画面，确保没有开启任何菜单及界面，并等待程序运行

10：程序运行期间，**请勿移动**键盘及鼠标，如果移动了极有可能造成**偏离**或**撞墙**的问题

## 配置文件说明
```json
{
    "real_width": 0, (实际宽度)
    "auto_battle_persistence": 0, (游戏内是否开启自动自动，填1则为开启)
    "real_height": 0, (实际长度)
    "map_debug": false,  (是否检测更新)
    "github_proxy": "", (github代理)
    "rawgithub_proxy": "", (github代理)
    "webhook_url": "",
    "start": true, (是否第一次运行脚本)
    "temp_version": "20230515205738",
    "star_version": "20230515220742",
    "open_map": "m", (打开地图按钮)
    "map_version": "20230515205738",
    "script_debug": true (是否检测脚本更新)
}
```

## 脚本录制 感谢[@AlisaCat](https://github.com/AlisaCat-S)

1：WASD移动，X是进战斗，鼠标左键是打障碍物，F键是交互，禁止用鼠标移动视角，只能使用方向键左右来移动视角（脚本运行后方向键左右会映射鼠标移动），录制期间能且只能按动键盘上的一个有效按键（也就是不能同时按下多键），脚本只会录制按键按下时间和移动的视角，不会录制停顿的时间（可以慢慢一个键一个键录制，保证录制准确性），录制完成后F9停止录制并保存。

2：完成后将会生成output(时间).json文件，请把他重命名替换成你要更改的地图json，并且将传送点截图重命名并保存到temp即可使用 （就可以申请到map分支提交，或者交给管理提交）

3：地图json中的空白填写示例：
```json
{
    "name": "乌拉乌拉-1",       （地图json名为1-1_1.json）
    "author": "Starry-Wind",   （作者名，第二作者不能覆盖第一作者名称）
    "start": [           （开局传送地图识别图片，并将鼠标移动至图片中间并按下按键）
        {"map": 1},         （按下m键打开地图）
        {"temp\\orientation_1.jpg": 1.5},     （识别到orientation_1.jpg图片后，将鼠标移动至图片中间并按下按键）
        {"temp\\map_1.jpg": 2},               （具体图片自己看，一般为该区域名"乌拉乌拉"的地图文字）
        {"temp\\map_1_point_1.jpg": 1.5},       （第一个传送点的图片）
        {"temp\\transfer.jpg": 1.5}              （"传送"字的图片）
    ]
}
```
 
## 注意事项
 
1：识图为截取游戏画面，所以不能有任何覆盖
 
2：支持地图 **空间站「黑塔」、雅利洛VI、仙舟「罗浮」**

3：如果你发现地图有撞墙问题，可以协助更新[地图文件提交到这里](https://github.com/Starry-Wind/StarRailAssistant/tree/map)

4：请使用**三月七**来跑图以获得最佳体验

⭐**如果喜欢，点个星星~**⭐

## 未来目标

1：模拟宇宙正在开发

2：GUI开发

3：后续将会新增找宝箱、锄大地顺带捡垃圾等功能

## 贡献者

感谢以下贡献者对本项目做出的贡献

<a href="https://github.com/Starry-Wind/StarRailAssistant/graphs/contributors">

  <img src="https://contrib.rocks/image?repo=Starry-Wind/StarRailAssistant" />

</a>

![Alt](https://repobeats.axiom.co/api/embed/79d87540c597fc0b30893860e7b92da60c555fa9.svg "Repobeats analytics image")

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Starry-Wind/Honkai-Star-Rail&type=Date)](https://star-history.com/#Starry-Wind/Honkai-Star-Rail&Date)
