#!/usr/bin/python3
if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[2] not in {"+", "-", "*", "/"}:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = {"+": add, "-": sub, "*": mul, "/": div}
    print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
    


