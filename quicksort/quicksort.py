#quicksort by Peng
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Quicksort(myList, start, end):
    if start<end:
        i, j = start, end
        n = myList[i]

        while i < j:
            while (i<j) and (myList[j] >= n):
                j = j-1

                myList[i] = myList[j]

            while (i<j) and (myList[i] <= n):
                i = i+1

                myList[j] = myList[i]

            myList[i] = n
        Quicksort(myList, start, i - 1)
        Quicksort(myList, j + 1, end)
    return myList

myList = [49,38,97,65,76,13,27,49]
print("Quick Sort: ")
Quicksort(myList,0,len(myList)-1)
print(myList)