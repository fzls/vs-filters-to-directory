_indent_level = 0


def indent() -> str:
    return '\t' * _indent_level


def inc_indent():
    global _indent_level
    _indent_level += 1


def dec_indent():
    global _indent_level
    _indent_level -= 1


def debug_print(msg, *arg, **kwargs):
    print(indent() + msg, *arg, **kwargs)


def with_indent(func):
    def inner(*args, **kwargs):
        inc_indent()
        func(*args, **kwargs)
        dec_indent()

    return inner
