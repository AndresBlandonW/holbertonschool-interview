#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Unlock boxes method"""
    unlockBox = list(range(1, len(boxes)))
    keys = boxes[0]

    for key in keys:
        if key in unlockBox:
            unlockBox.remove(key)
            keys.extend(boxes[key])

    if unlockBox:
        return False

    return True
