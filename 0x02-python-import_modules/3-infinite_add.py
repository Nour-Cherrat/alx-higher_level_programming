#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    value = 0
    for arg in sys.argv[1:]:
        value = value + int(arg)
    print("{}".format(value))
