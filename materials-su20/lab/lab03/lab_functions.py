from datascience import *

def draw_scatter_chart(*args):
    if len(args) % 2 != 0:
        raise ValueError("This function requires an even number of arguments,"
                         "but you have given it {:d}".format(len(args)))
    data = Table().with_columns("x", args[::2], "y", args[1::2])
    data.scatter("x")
