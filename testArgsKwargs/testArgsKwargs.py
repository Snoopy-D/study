# -*- coding: utf-8 -*-

import functools

def print_func_name():
    def decorator(func):
        functools.wraps(func)
        def wrapper(*args, **kwargs):
            print func.__name__, args, kwargs
            func(*args, **kwargs)
        return wrapper
    return decorator

tempList = [1, 2, 3]
tempTuple = (2, 3, 4)
tempDict = {'s':3, 'm':4, 'c':5}

# 如果不确定往一个函数中传入多少参数，或者希望以元组(tuple)或者列表(list)的形式传参数的时候，可以使用*args
# 如果不知道往函数中传递多少个关键词参数或者想传入字典的值作为关键词参数的时候，可以使用**kwargs
@print_func_name()
def testFunc(*args, **kwargs):
    print args, kwargs

testFunc()
testFunc(*tempList)
testFunc(*tempTuple)
testFunc(*tempDict)
testFunc(**tempDict)
testFunc(*tempList, **tempDict)
testFunc(0)
testFunc(0, *tempList)
testFunc(0, **tempDict)
testFunc(0, *tempList, tempName = 'bye', **tempDict)
pass