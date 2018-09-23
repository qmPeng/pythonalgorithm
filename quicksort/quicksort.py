# quicksort by Peng
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def QuickSort(myList, start, end):
    if start < end:
        i, j = start, end
        n = myList[i]

        while i < j:
            while (i < j) and (myList[j] > n):
                j -= 1

            myList[i] = myList[j]

            while (i < j) and (myList[i] <= n):
                i += 1

            myList[j] = myList[i]

        myList[i] = n
        QuickSort(myList, start, i - 1)
        QuickSort(myList, i + 1, end)
    return myList


myList = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
print("initial array:\n", myList)
print("Quick Sort: ")
QuickSort(myList, 0, len(myList) - 1)
print(myList)
