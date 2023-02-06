#!/usr/bin/python3
"""
checks if all boxes can be opened with keys contained
in the other boxes
"""


def canUnlockAll(boxes):
    """
    Argument: a method that determines if all the boxes can be opened
    Boxes - a list of lists.
    Returns true if all boxes can be opened else false..
    Uses indexes as keys.
    """
    sbox = []
    sbox.append(boxes[0])
    for list in boxes:
        for d in list:
            if d < len(boxes) and list != boxes[d]:
                if boxes[d] not in sbox:
                    sbox.append(boxes[d])
    return len(sbox) == len(boxes)
