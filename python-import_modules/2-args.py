#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
if len(argv) == 0:
    print("{} arguments.".format(len(argv)))
elif len(argv) == 1:
    print("{} argument:".format(len(argv)))
else:
    print("{} arguments:".format(len(argv)))

i = 1
while i <= len(argv):
    print("{}: {}".format(i, sys.argv[i]))
    i += 1
