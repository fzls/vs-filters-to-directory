import argparse

from filter import filter_to_directory
from link import LINK_TYPE_SOFT, LINK_TYPE_HARD
from util import run_as_admin, pause


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root_dir", default=".", type=str, help="要处理的根目录，将递归处理下方各个项目子目录")
    parser.add_argument("-l", "--link_dir_name", default="_filter_links", type=str, help="各个项目中生成的链接文件夹名称")
    parser.add_argument("--link_type", default=LINK_TYPE_SOFT, choices=[LINK_TYPE_SOFT, LINK_TYPE_HARD], help="链接类型，默认为soft。推荐使用soft，可结合clion的插件 IDEA Resolve Symlinks 实现自动打开链接的实际文件")

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    if args.link_type == LINK_TYPE_SOFT:
        run_as_admin()

    filter_to_directory(args.root_dir, args.link_dir_name, args.link_type)

    pause("filter层级链接目录生成完毕")


if __name__ == "__main__":
    main()
