def left_sum(func, args, h):
    return sum(h * func(arg) for arg in args[:-1])


def right_sum(func, args, h):
    return sum(h * func(arg) for arg in args[1:])


def center_sum(func, arguments, h):
    return sum(h * func((arguments[i] + arguments[i + 1]) / 2) for i in range(len(arguments) - 1))


def trapezoid_sum(func, args, h):
    argf = [func(arg) for arg in args]
    return sum(h * (argf[i] + argf[i + 1]) / 2 for i in range(len(argf) - 1))


def parabolic_sum(func, args, h):
    return sum(h * (func(args[i]) + func(args[i + 1]) + 4 * func((args[i] + args[i + 1]) / 2)) / 6 for i in range(len(args) - 1))
