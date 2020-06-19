"""
Bubble sort : The bubble sort algorithm repeatedly scans through the list,
    comparing adjacent elements and swapping them if they are in wrong order.
"""
def bubble(list1):
    for i in range(1 ,x): #number of passes n-1 passes 
        for j in range(0 , x-i ): #comparison .. x-i because there is no need to compare list item after 1 compariosion 
            if list1[j] > list1[j+1]:
                temp = 0
                temp = list1[j]
                list1[j]= list1[j+1]
                list1[j+1] = temp
            else:
                continue
            print(list1)
x = int(input("Enter the total number of elements in a list : ")) 
list1 = [ ]
for i in range(x): # taking values of list 
    list1.append(input("Enter number {} \t ".format(i+1)))  
bubble(list1)
"""
Order of growth ----> Quadratic ----> BIG O (n^2)
algorithm is best suitable for smaller data sets
"""