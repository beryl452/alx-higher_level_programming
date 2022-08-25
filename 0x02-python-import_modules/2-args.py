#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    i = 1
    j = len(argv)
    if j == 0:
        print("{:d} arguments.".format(j))
    elif len(argv) == 1:
        print("{:d} argument:".format(j))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(j))
        while i <= j:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
