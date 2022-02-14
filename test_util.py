from util import remove_suffix


def test_remove_suffix():
    assert remove_suffix("/home/user/file.txt", ".txt") == "/home/user/file"
