import os
import traceback
import time
import ctypes
import pyuac
import questionary
import logging

from get_width import get_width, check_mult_screen
from tools.config import read_json_file, modify_json_file, init_config_file, CONFIG_FILE_NAME
from tools.map import Map
from tools.update_file import update_file_main
from tools.switch_window import switch_window
from tools.exceptions import Exception
from tools.log import log, webhook_and_log


from_star_list = {"空间站「黑塔」": "1", "雅利洛-VI": "2", "仙舟「罗浮」": "3"}


def choose_map(map_instance: Map):
    title_ = "请选择起始星球："
    options_map = list(from_star_list.keys())
    option_ = questionary.select(title_, options_map).ask()
    main_map = from_star_list.get(option_)
    title_ = "请选择起始地图："
    options_map = map_instance.map_list_map.get(main_map)
    if not options_map:
        return None
    keys = list(options_map.keys())
    values = list(options_map.values())
    option_ = questionary.select(title_, values).ask()
    side_map = keys[values.index(option_)]
    return f"{main_map}-{side_map}"


def main():
    main_start()
    map_instance = Map()
    start = choose_map(map_instance)
    if start:
        log.info("脚本将自动切换至游戏窗口，请保持游戏窗口激活")
        check_mult_screen()
        switch_window()
        time.sleep(0.5)
        get_width()
        log.info("开始运行，请勿移动鼠标和键盘")
        log.info("若脚本运行无反应,请使用管理员权限运行")
        map_instance.auto_map(start)  # 读取配置
    else:
        log.info("错误编号，请尝试检查更新")
        webhook_and_log("脚本已经完成运行")

def main_start():
    if not read_json_file(CONFIG_FILE_NAME, False).get('start'):
        title = "请选择下载代理地址：（不使用代理选空白选项）"
        options = ['https://ghproxy.com/', 'https://ghproxy.net/', 'hub.fgit.ml', '']
        option = questionary.select(title, options).ask()
        modify_json_file(CONFIG_FILE_NAME, "github_proxy", option)
        title = "请选择代理地址：（不使用代理选空白选项）"
        options = ['https://ghproxy.com/', 'https://ghproxy.net/', 'raw.fgit.ml', 'raw.iqiq.io', '']
        option = questionary.select(title, options).ask()
        modify_json_file(CONFIG_FILE_NAME, "rawgithub_proxy", option)
        title = "你游戏里开启了连续自动战斗吗？："
        options = ['没打开', '打开了', '这是什么']
        option = questionary.select(title, options).ask()
        modify_json_file(CONFIG_FILE_NAME, "auto_battle_persistence", options.index(option))
        modify_json_file(CONFIG_FILE_NAME, "start", True)


def up_data():
    ghproxy = read_json_file(CONFIG_FILE_NAME, False).get('github_proxy', "")
    rawghproxy = read_json_file(CONFIG_FILE_NAME, False).get('rawgithub_proxy', "")

    if not read_json_file(CONFIG_FILE_NAME, False).get('map_debug'):
    
        # update map files
        up_map = {
            'url_proxy': ghproxy,
            'raw_proxy': rawghproxy,
            'skip_verify': False,
            'type': "map",
            'version': "map",
            'url_zip': "https://github.com/Starry-Wind/Honkai-Star-Rail/archive/refs/heads/map.zip",
            'unzip_path': "map",
            'keep_folder': [],
            'keep_file': [],
            'zip_path': "Honkai-Star-Rail-map/",
            'name': "地图"
        }
        update_file_main(**up_map)

        # update temp files
        up_temp = {
            'url_proxy': ghproxy,
            'raw_proxy': rawghproxy,
            'skip_verify': False,
            'type': "temp",
            'version': "map",
            'url_zip': "https://github.com/Starry-Wind/Honkai-Star-Rail/archive/refs/heads/map.zip",
            'unzip_path': "temp",
            'keep_folder': [],
            'keep_file': [],
            'zip_path': "Honkai-Star-Rail-map/",
            'name': "图片"
        }
        update_file_main(**up_temp)

        # update script files
        if not read_json_file(CONFIG_FILE_NAME, False).get('script_debug', False):
            up_script = {
                'url_proxy': ghproxy,
                'raw_proxy': rawghproxy,
                'skip_verify': False,
                'type': "star",
                'version': "beta-2.7_test",
                'url_zip': "https://github.com/Starry-Wind/Honkai-Star-Rail/archive/refs/heads/beta-2.7_test.zip",
                'unzip_path': ".",
                'keep_folder': ['.git', 'logs', 'temp', 'map', 'tmp', 'venv'],
                'keep_file': ['config.json', 'version.json', 'star_list.json'],
                'zip_path': "Honkai-Star-Rail-beta-2.7_test/",
                'name': "脚本"
            }
            update_file_main(**up_script)
    else:
        log.info("您没有更新脚本的权限")



if __name__ == "__main__":
    try:
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
        else:
            title = "请选择操作"
            options = ['启动脚本', '检查更新']
            option = questionary.select(title, options).ask()
            if option == "启动脚本":
                main()
            elif option == "检查更新":
                up_data()
    except ModuleNotFoundError as e:
        log.error(traceback.format_exc())
        os.system("pip install -r requirements.txt")
        log.info("请重新运行")
    except NameError as e:
        log.error(traceback.format_exc())
        os.system("pip install -r requirements.txt")
        log.info("请重新运行")
    except Exception as e:
        log.error(traceback.format_exc())
