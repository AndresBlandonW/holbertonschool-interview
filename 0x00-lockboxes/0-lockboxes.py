#!/usr/bin/python3

def canUnlockAll(boxes):
    """Unlock boxes method"""
    can = len(boxes) - 1
    unlockBox = []

    unlockBox.append(0)
    for i in range(0, can):
        items = len(boxes[i])
        for x in range(0, items):
            if x in unlockBox != True:
                unlockBox.append(x)
    
    if len(unlockBox) == can+1:
       return True
    else:
        return False
