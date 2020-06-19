# -*- coding: utf-8 -*-
"""
Selection sort - Selection sort scans through the list iteratively, selecting 
    one item in each scan, and moving the item to its correct position in the list 
"""
list1 = [105 , 120 , 10 ,200 ,20]
print(list1)
node = 0
for i in range(0, len(list1)):
    smallest = list1[i]
    for j in range(i, len(list1)):
        if list1[j] <= smallest :
            smallest = list1[j]
            node = j
        else:
            continue
    temp = 0 
    temp = list1[i]
    list1[i] = smallest
    list1[node] = temp
    print(list1)
