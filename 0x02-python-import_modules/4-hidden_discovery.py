#!/usr/bin/python3
import sys
import hidden_4 as hide

if __name__ != "__main__":
    exit()

for z in dir(hide):
    if z[0:2] != "__":
        print(z)
