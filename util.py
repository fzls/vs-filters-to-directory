import os
import pathlib
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
        s = s[:-len(suffix)]

    return s


def make_sure_dir_exists(dir_path):
    # debug_print("make_sure_dir_exists: " + dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
