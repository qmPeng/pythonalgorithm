#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mergeSort(myList):
    if len(myList) == 0:
        print('There is no item in the list')
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        # i, j, k = 0, 0, 0
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


arr = [64, 36, 93, 27, 55, 13, 24, 87, 26]
print("Origin: ", arr)
mergeSort(arr)
print("Result: ", arr)
