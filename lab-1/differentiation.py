def atpoint_right_diff(func, arg, h):
    return (func(arg + h) - func(arg)) / h


def right_diff(func, arg, h):
    return [atpoint_right_diff(func, x, h) for x in arg]


def atpoint_left_diff(func, arg, h):
    return (func(arg) - func(arg - h)) / h


def left_diff(func, arg, h):
    return [atpoint_left_diff(func, x, h) for x in arg]


def atpoint_diff(func, arg, h):
    return (func(arg + h) - func(arg - h)) / (2 * h)


def diff(func, arg, h):
    return [atpoint_diff(func, x, h) for x in arg]