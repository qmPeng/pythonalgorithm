#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonds.basic.stack import Stack


def revstring(myList):

    s = Stack()
    rev = ''

    for item in myList:
        s.push(item)

    while not s.isEmpty():
        if rev == '':
            rev = s.pop()
        else:
            rev = rev + ', ' + s.pop()
    return rev


arr = ['mon', 'tue', 'wed', 'thu', 'fri']
print('origin:', arr)
print('result:', revstring(arr))
