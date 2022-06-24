#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """set represents a valid UTF-8 encoding"""
    if data == []:
        return True

    length = len(data)
    mask = 255
    index = 0
    while (index < length):
        if data[index] < 0 or type(data[index]) is not int:
            return False
        try:
            d = data[index] & mask

            if d > 127 and d < 192:
                return False

            if d > 193 and d < 224:
                byte_two = data[index + 1] & mask
                if byte_two > 127 and byte_two < 192:
                    index += 1
                else:
                    return False

            if d > 223 and d < 240:
                byte_two = data[index + 1] & mask
                byte_three = data[index + 2] & mask
                if (byte_two > 127 and byte_two < 192)\
                        and (byte_three > 127 and byte_three < 192):
                    index += 2
                else:
                    return False

            if d > 239 and d < 245:
                byte_two = data[index + 1] & mask
                byte_three = data[index + 2] & mask
                byte_four = data[index + 3] & mask
                if (byte_two > 127 and byte_two < 192)\
                        and (byte_three > 127 and byte_three < 192)\
                        and (byte_four > 127 and byte_four < 192):
                    index += 3
                else:
                    return False
        except IndexError:
            return False
        else:
            index += 1
    return True
