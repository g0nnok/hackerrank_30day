#!/bin/python
def quick_sort(arr):
#    print arr
    if len(arr) <= 1 :
#        print arr
        return arr
    pivot = arr[0]
    left = []
    right = []
    sorted = []
    for i in arr:
        if i == pivot:
            continue
        elif i > pivot:
            right.append(i)
        else:
            left.append(i)
    l = quick_sort(left)
    r = quick_sort(right)
    for i in l:
        sorted.append(i)
    sorted.append(pivot)
    for i in r:
        sorted.append(i)
    print sorted
    return sorted

m = input()
ar = [int(i) for i in raw_input().strip(' ').split()]
quick_sort(ar)

