#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shellSort(myList):
    sublistcount = len(myList) // 3
    while sublistcount > 0:
        for start in range(sublistcount):
            gapInsertionSort(myList, start, sublistcount)
        sublistcount = sublistcount // 3


def gapInsertionSort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentvalue


myList = [64, 36, 93, 27, 55, 13, 24, 87, 26]
shellSort(myList)
print(myList)
