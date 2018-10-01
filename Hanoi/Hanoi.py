#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def hanoi(height, start, helper, end):

    if height == 1:
        print(start, '-->', end)
    else:
        hanoi(height-1, start, end, helper)
        print(start, '-->', end)
        hanoi(height-1, helper, start, end)


hanoi(4, 'A', 'B', 'C')
