#!/usr/bin/python
# Program to take a Cisco ACL and cleanup the line numbers ##

import sys
import getopt

x = 0
count = 0
acl = inputfile = outputfile = ''


def usage(ext):
    # exit with description and command line example
    print("\nCisco ACL re-numbering utility")
    print("usage:")
    print("-h <help> -- this message")
    print(("%s -i <input file> -o <output file>" % sys.argv[0]))
    print("  note: if output is not specified, it will be sent to <stdout>")
    sys.exit(ext)

# get command line options
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h:i:o:')
except getopt.GetoptError:
    usage(2)

# if no command line options given, exit
if not opts:
    usage(0)

# command line options parsing
for opt, arg in opts:
    if opt == ('-h'):
        usage(0)
    elif opt in ("-i", "--ifile"):
        inputfile = open(arg, 'r')
    elif opt in ("-o", "--ofile"):
        outputfile = open(arg, 'w')

# process input file
for line in inputfile:
    count += 1
    s = line.strip().split(" ", 1)
    if s[0].isdigit():
        x += 10
        acl = str(x) + " " + s[1]
    else:
        acl = line.strip()

    if outputfile:
        outputfile.write("%s\n" % acl)
    else:
        print(acl)

# close files before exiting
if inputfile:
    inputfile.close()
if outputfile:
    outputfile.close()

print(("\n\n Processed %s lines." % count))
