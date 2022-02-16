import pathlib
from os import path

import bs4

from debug import debug_print, with_indent
from link import make_link, LINK_TYPE_SOFT
from util import make_sure_dir_exists, remove_duplicate_filters, pause, remove_directory


def filter_to_directory(root_dir: str, link_dir_name: str, link_type: str = LINK_TYPE_SOFT):
    # 找到目录（及子目录）中所有的 vc项目 filters 文件
    filter_files = list(pathlib.Path(root_dir).glob("**/*.vcxproj.filters"))

    # 移除其中不同vs版本的重复文件，如xxx.vcxproj.filters, xxx_2012.vcxproj.filters, xxx_2019.vcxproj.filters
    filter_files = remove_duplicate_filters(filter_files)

    if len(filter_files) == 0:
        print(f"{root_dir} 及其子目录中没有找到任何 filters 文件，将不执行任何操作")
        return

    # 为每个 filters 文件生成对应的目录
    for idx_filter, filter in enumerate(filter_files):
        debug_print(f"{idx_filter + 1}/{len(filter_files)}: 开始处理 {filter}")

        try:
            process_filter(filter, link_dir_name, link_type)
            debug_print("\n")
        except Exception as e:
            debug_print(f"处理 {filter} 时出错，请检查：{e}")
            pause("请检查上述错误后，按任意键继续处理后续filter")


@with_indent
def process_filter(filter, link_dir_name, link_type):
    soup = bs4.BeautifulSoup(filter.read_text(encoding="utf-8"), "lxml")
    project_dir = path.dirname(path.realpath(filter))
    link_dir = path.join(project_dir, link_dir_name)

    # 移除之前生成的链接目录
    remove_directory(link_dir)

    for item_group in soup.find_all("itemgroup"):
        for item in item_group.children:
            if item.name == "filter":
                # 对于filter，生成对应层级的目录结构
                filter_name = item.attrs["include"]

                filter_target_dir = path.join(link_dir, filter_name)

                debug_print(f"filter : {filter_name}")
                make_sure_dir_exists(filter_target_dir)
            elif item.name is not None:
                # 对于其他条目，则在其filter对应目录下，生成该条目末端的文件名部分的链接，指向该条目路径
                source_file_relative_path = item.attrs["include"]
                filter_name = ""
                if item.filter is not None:
                    filter_name = f"{item.filter.text}"

                link_path = path.join(link_dir, filter_name, path.basename(source_file_relative_path))
                link_target = path.join(project_dir, source_file_relative_path)

                debug_print(f"item   : {item.attrs['include']}")
                make_link(link_path, link_target, common_prefix_len=len(project_dir) + 1, link_type=link_type)
