#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonds.basic.stack import Stack
def parCheck(string):
    s = Stack()
    balanced = True
    i = 0
    while i < len(string) and balanced:
        symbol = string[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        i = i + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parCheck('((()))'))
print(parCheck('(()'))