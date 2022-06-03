#!/usr/bin/python3
import sys
import re


if __name__ == "__main__":
    lines = 1
    fileSize = 0
    listCodes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                 '404': 0, '405': 0, '500': 0}
    try:
        for data in sys.stdin:
            codes = re.search('1" (.*)', data).group(1).split(" ")
            statusCode = codes[0]
            fileSize = fileSize + int(codes[1])

            # Check valid status code
            if (statusCode in listCodes):
                listCodes[statusCode] += 1

            if (lines == 10):
                listFinal = []
                for key in listCodes:
                    if (listCodes[key] != 0):
                        listFinal.append(key + ': ' + str(listCodes[key]))

                listFinal.sort()
                print('File size: {}'.format(fileSize))
                for x in range(len(listFinal)):
                    print(listFinal[x])
                lines = 1
            else:
                lines = lines + 1
    except KeyboardInterrupt:
        listFinal = []
        for key in listCodes:
            if (listCodes[key] != 0):
                listFinal.append(key + ': ' + str(listCodes[key]))

        listFinal.sort()
        print('File size: {}'.format(fileSize))
        for x in range(len(listFinal)):
            print(listFinal[x])
        lines = 1
