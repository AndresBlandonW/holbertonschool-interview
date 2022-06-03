#!/usr/bin/python3
"""Project log parsing"""
from sys import stdin, stdout
import re


if __name__ == "__main__":
    # show data
    lines = 0
    fileSize = 0
    listCodes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                 '404': 0, '405': 0, '500': 0}
    try:
        for data in stdin:
            # check empty
            if data == "":
                continue

            codes = re.search('1" (.*)', data).group(1).split(" ")
            statusCode = codes[0]
            fileSize = fileSize + int(codes[1])

            # Check valid status code
            if (statusCode in listCodes):
                listCodes[statusCode] += 1

            lines += 1
            if (lines % 10 == 0):
                print('File size: {}'.format(fileSize))
                for key in sorted(listCodes):
                    print("{}: {}".format(key, listCodes[key]))

        print('File size: {}'.format(fileSize))
        for key in sorted(listCodes):
            print("{}: {}".format(key, listCodes[key]))

    except KeyboardInterrupt as e:
        print('File size: {}'.format(fileSize))
        for key in sorted(listCodes):
            print("{}: {}".format(key, listCodes[key]))

        raise
