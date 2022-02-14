import argparse

from filter import filter_to_directory


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root_dir", default=".", type=str, help="要处理的根目录，将递归处理下方各个项目子目录")
    parser.add_argument("-l", "--link_dir_name", default="_filter_links", type=str, help="各个项目中生成的链接文件夹名称")

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    filter_to_directory(args.root_dir, args.link_dir_name)


if __name__ == '__main__':
    main()
