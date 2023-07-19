#!/usr/bin/env python3

for i in range(10):
    for j in range(i + 1, 10):
        print("{:01d}".format(i) + "{:01d}".format(j), end=", " if j < 9 else "\n")



