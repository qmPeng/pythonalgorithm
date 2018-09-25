#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insertionSort(myList):
    for i in range(1, len(myList)):
        rightvalue = myList[i]
        position = i

        while position > 0 and myList[position-1] > rightvalue:
            myList[i] = myList[position-1]
            position = position -1

        myList[position] = rightvalue



arr = [64,25,93,37,66,38,24,75,26]
insertionSort(arr)
print(arr)
