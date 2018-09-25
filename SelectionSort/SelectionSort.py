#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def selectionSort(myList):
    if len(myList)==0:
        print("There is no item in the list")
    elif len(myList)==1:
        return myList
    else:
        for slot in range(len(myList)-1, 0, -1):
            positionOfMax = 0
            for position in range(1, slot+1):
                if myList[position]>myList[positionOfMax]:
                    positionOfMax = position
            temp = myList[slot]
            myList[slot] = myList[positionOfMax]
            myList[positionOfMax] = temp


myList = [64, 36, 93, 27, 55, 13, 24, 87, 26]
selectionSort(myList)
print(myList)