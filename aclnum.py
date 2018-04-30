#!/usr/bin/python
# Program to take a Cisco ACL and cleanup the line numbers ##

from __future__ import print_function
import sys


def usage(ext):
    # exit with description and command line example
    print("\nCisco ACL re-numbering utility")
    print("   Renumber a Cisco ACL to increment by 10.")
    print("\nusage:")
    print(("\n%s <input file>" % sys.argv[0]))
    sys.exit(ext)


def main():
    STEP = 10  # number to increment lines by
    count = 0
    acl, inputfile = "", ""

    try:
        inputfile = open(sys.argv[1], "r")
    except (IndexError, IOError):
        usage(0)

    # process input file
    for line in inputfile:
        s = line.strip().split(" ", 1)
        if s[0].isdigit():
            count += 1
            acl = " " + str(count * STEP) + " " + s[1]
        else:
            acl = line.strip()
        print(acl)

    # close files before exiting
    if inputfile:
        inputfile.close()

    print(("\n\n!!Processed %s lines." % count))
    sys.exit(0)


if __name__ == "__main__":
    main()
