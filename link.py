import os
from os import path

from debug import debug_print, with_indent
from util import make_sure_dir_exists

LINK_TYPE_SOFT = "soft"
LINK_TYPE_HARD = "hard"


@with_indent
def make_link(link_path: str, link_target: str, common_prefix_len: int = 0, link_type: str = LINK_TYPE_SOFT):
    debug_print(f"Creating {link_type} link: {link_path[common_prefix_len:]} -> {link_target[common_prefix_len:]}")

    if not path.exists(link_target):
        print(f"target={link_target} does not exist")
        return

    make_sure_dir_exists(path.dirname(link_path))

    if path.exists(link_path):
        os.remove(link_path)

    if link_type == LINK_TYPE_SOFT:
        os.symlink(link_target, link_path)
    else:
        os.link(link_target, link_path)
