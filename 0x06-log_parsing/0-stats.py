#!/usr/bin/python3
"""Project log parsing"""
from sys import stdin, stdout


if __name__ == "__main__":
    # show data
    lines = 0
    fileSize = 0
    listCodes = {}
    try:
        for data in stdin:
            # check empty
            if data == "":
                continue

            statusCode = data.split()[-2]
            fileSize += int(data.split()[-1])

            # Check valid status code
            if (statusCode in listCodes):
                listCodes[statusCode] += 1
            else:
                listCodes[statusCode] = 1

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
