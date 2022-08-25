#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    argc = len(userin)
    print("{:d} {:s}{:s}".
          format(argc,
                 "arguments" if (argc) is not 1 else "argument",
                 "." if (argc) is 0 else ":"))
    for index, arg in enumerate(userin):
        print("{:d}: {:s}".format(index + 1, arg))
