#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubbleSort(myList):
    for passnum in range(len(myList)-1,0,-1):
        for i in range(passnum):
            if myList[i] > myList[i+1]:
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp


myList = [64, 36, 93, 27, 55, 13, 24, 87, 26]
bubbleSort(myList)
print(myList)
