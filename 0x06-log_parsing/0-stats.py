#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
from sys import stdin, stdout
import traceback


if __name__ == "__main__":
    # save as a dict using key/value
    listCodes = {}
    file_size = 0
    lines = 0
    try:
        # open and read file
        for line in stdin:
            # Check if line is empty
            if line == "":
                continue

            file_size += int(line.split()[-1])
            status_code = line.split()[-2]

            if status_code in listCodes:
                listCodes[status_code] += 1
            else:
                listCodes[status_code] = 1

            lines += 1

            if lines % 10 == 0:
                print("File size: {}".format(file_size))

                for k in sorted(listCodes):
                    print("{}: {}".format(k, listCodes[k]))

        print("File size: {}".format(file_size))

        for k in sorted(listCodes):
            print("{}: {}".format(k, listCodes[k]))

    except KeyboardInterrupt as e:
        print("File size: {}".format(file_size))

        for k in sorted(listCodes):
            print("{}: {}".format(k, ListCodes[k]))

        raise
