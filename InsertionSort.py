"""
Insertion sort 
"""
list1 = [70 , 80 , 30 ,10 , 20]
for i in range(0 , len(list1)):
    current = list1[i]
    position = i 
    while position > 0 and current <= list1[position - 1 ] :
        temp = 0
        temp = list1[position - 1]
        list1[position - 1 ] = current
        list1[position] = temp
        position -= 1
    print(list1)
