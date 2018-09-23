# quicksort by Peng
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def QuickSort(myList, start, end):
    if start < end:
        divIndex = Partition(myList, start, end)

        QuickSort(myList, start, divIndex)
        QuickSort(myList, divIndex + 1, end)
    else:
        return


def Partition(myList, start, end):
    i = start - 1
    for j in range(start, end):
        if myList[j] <= myList[end]:
            i = i + 1
            myList[i], myList[j] = myList[j], myList[i]
    myList[i + 1], myList[end] = myList[end], myList[i + 1]
    return i


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]

print("initial array:\n", arr)
QuickSort(arr, 0, len(arr) - 1)
print("result array:\n", arr)