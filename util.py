import ctypes
import os
import pathlib
import platform
import sys
from typing import List


def remove_duplicate_filters(filters: List[pathlib.Path]) -> List[pathlib.Path]:
    normalized_project_path_set = set()
    unique_filters = []

    for filter in filters:
        normalized_project_path = str(filter)
        normalized_project_path = remove_suffix(normalized_project_path, ".vcxproj.filters")
        normalized_project_path = remove_suffix(normalized_project_path, "_2012")
        normalized_project_path = remove_suffix(normalized_project_path, "_2019")
        if normalized_project_path in normalized_project_path_set:
            continue
        normalized_project_path_set.add(normalized_project_path)

        unique_filters.append(filter)

    return unique_filters


def remove_suffix(s: str, suffix: str) -> str:
    if s.endswith(suffix):
        s = s[: -len(suffix)]

    return s


def make_sure_dir_exists(dir_path):
    # debug_print("make_sure_dir_exists: " + dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)


# base on https://gist.github.com/GaryLee/d1cf2089c3a515691919
def run_as_admin():
    if not is_windows():
        return

    shell32 = ctypes.windll.shell32
    if shell32.IsUserAnAdmin():
        return True

    argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = argv[1:]
    else:
        arguments = argv
    argument_line = " ".join(arguments)
    executable = sys.executable

    print("当前链接类型为软链接，在windows下需要管理员权限，请在弹出的uac框中选择确认，从而使用管理员权限运行。参数信息如下:\n\t", executable, argument_line)

    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False

    print("run_as_admin ok, exit current process, actual work will be done by elevated process")
    exit(0)


def is_windows():
    return platform.system() == "Windows"


def pause(ctx: str = ""):
    if ctx != "":
        print(ctx)

    if is_windows():
        pause_cmd = "PAUSE"
    else:
        pause_cmd = 'read -r -p "Press Enter to continue..." key'
    os.system(pause_cmd)
