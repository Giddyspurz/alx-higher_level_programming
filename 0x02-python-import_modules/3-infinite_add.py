#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    sum = 0
    if size > 1:
        for z in range(1, size):
            sum += int(sys.argv[z])
    print("{}".format(sum))
