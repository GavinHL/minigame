
def print_str(*lst):
    for i in lst:
        if isinstance(i, str):
            print i.decode("utf8"),
        else:
            print i,
    print
