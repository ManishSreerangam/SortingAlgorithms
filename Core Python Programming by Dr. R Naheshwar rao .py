"""
Core Python Programming by Dr. R Naheshwar rao 
"""
# program-1  -- sum of two complex numbers 
c1 = 1.2 + 3.5j
c2 = 2.8 + 2.1j
c = c1 + c2 
print ("sum = " , c )

# program-2 -- convert 0o, ob , ox into a decimal number system 
a = 0o17
int(a)
print(a)
print(bin(a)) #converts into binary 
print(hex(a))
# create a byte type array ....read and display the elements 
ele = [225 , 0 , 24 , 3, 10]
a = bytes(ele)
for i in a:
    print(i)
    print(type(i))
b = bytearray(ele)
for i in b:
    print(i)
b[0] = 27
for i in b:
    print(i)
list1 = [1 , "MAnish Sreerangam" , 255 ]
for i in list1:
    print(i)
int1 = int(input("Enter first number : "))
int2 = int(input("Enter Second number : "))
print(" You have entered :   %d , %d " %(int1, int2))
print("The sum of the give two numbers i.e {} and  {} is {}".format(int1 , int2 , int1 + int2))
print(" The product of the same two numbers is i.e {} and {} is {}".format(int1 , int2 , int1 * int2))
int5 = input("Enter a hexa-decimal number : ")
print(int(int5, 16))
in1 , in2 , in3 = [int(i) for i in input("Enter 3 number : ").split()]
print("Sum = " , in1+in2+in3)
i1 , i2 , i3 = [int(i) for i in input("Enter 3 number with commas : ").split(",")]
print("Sum = " , i1+i2+i3)
i1 , i2 , i3 = [i for i in input("Enter 3 strings with commas : ").split(",")]
print("Sum = " , i1+i2+i3)
int1 = input("enter a list of elemets: ")
print(int1)
print(type(int1))
int1 = []
for i in range(0,4):
    a = int(input("enter a number"))
    int1.append(a)
print(int1)
print(type(int1))
int1 = eval(input("enter a list of elemets: "))
print(int1)
print(type(int1))
#printing area of a circle 
import math 
radius = float(input("Enter the radius of a circle : "))
area_of_a_circle = math.pi * radius**2
print("The area of the circle is : {:.02f}".format(area_of_a_circle))

i = int(input("Enter a number : "))
if i == 1 :
    print("the number is one ")
str1 = True
if str1 == True:
    print("Hello World")
#odd or even 
int1 = int(input("Enter a number "))
if int1 % 2 == 0 :
    print("The given number i.e {} is divisible by 2 ".format(int1))
else:
    print("Number is odd ")
# To check wether a number is in between 1 and 10 
int1 = int(input("Enter a number : "))
if int1 > 1 and int1 < 10:
    print(" The given number i.e {} lies between 1 and 10 ".format(int1))
#if a given number is zero, positive and negative 
int1 = int(input("Enter a number : "))
if int1 > 0 :
    print("The given number i.e {} is greater than zero. ".format(int1))
elif int1 < 0 :
    print("The given number i.e {} is less than zero ".format(int1))
else:
    print("The number is equal to zero.")
int1 = 0
while int1 <= 10 :
    print(int1)
    int1 += 1
#to display all even numbers between 0 and 200 
int1 = 0
while int1 <= 200 :
    if int1 % 2 == 0:
        print(" {} is an even number ".format(int1))
    int1 += 1
# even numbers between m and n 
m , n = [int(i) for i in input("enter the starting and ending values ").split(",")]
print("{} , {} is the starting and the ending numbers".format(m , n))
while m <= n :
    if m % 2 == 0 :
        print (" {} is an even number ". format(m))
    m += 1
str1 = input("Enter a string : ")
print("The length of the string is : {} ".format(len(str1)))
for i in str1 :
    print(i)
print("Printing number using a sequence index")
for i in range(0 , len(str1)):
    print(str1[i])
#odd numbers from 1 to 10 using a range function 
for i in range(0 , 10 ):
    if i % 2 != 0:
        print("the number i.e {} is an odd number ".format(i))
#numbers to be displayed from 1 to 10 in desending order 
for i in range (10 , 0 , -1 ):
    print(i)
lis1 = [10 , 20 , 30 , "manish sreerangam "]
for i in lis1 :
    print(i)
#total sum of numbers in a list 
lis1 = [10 , 20 , 30 , 40.05]
print("The length of the list is {}".format(len(lis1)))
sum = 0
for i in lis1:
    sum += i
print("The sum of elements in the list i.e {} is equal to {}".format(lis1 , sum))
while i <= len(lis1):
    sum += len[i]
print("The sum of elements in the list i.e {} is equal to {}".format(lis1 , sum))
#right angled triangle 
for i in range( 1 ,6 ):
    for j in range (0 , i ):
        print("*" , end =" ")
    print(" ")
starting = 0 
ending = 3 
for i in range(starting, ending ):
    for j in range (i , ending-1 ):
        print(" " , end = " ")
    for k in range (0, i+1):
        print("*" , end = " ")
    print(" ")

for i in range ( 1 , 11 ):
    for j in range (1 , 11 ):
        print("{}".format(i*j) , end = "\t")       
    print(" ")
lis1 = [10 , 25 , 35 , 45 , 24 , 78 , 95 , 124 , 33 , 55]
num = int(input("Enter a number which you want to search : "))
for i in lis1:
    if i == num :
        print("Yes the number which you wanted to search exists .")
        break
else:
    print("sorry ")
for i in range(10 , 0 , -1 ):
    if i <= 5:
        break
    else:
        print(i)

in1 = 0
while in1 <= 10 :
    if in1 <= 5:
        print(in1)
    else:
        continue
    in1 += 1 
#fibnacci series
current_number = 0
next_number = 1
i = 0
print(current_number)
while i <= 10 :
    
    print(next_number)
    temp = 0
    j = current_number + next_number
    temp = current_number
    current_number = next_number
    next_number = j
    i += 1
#array in python 
from array import *
a = array('i' , [1 , 2 , 3 ,4 ]) #array for integers
b = array('u' , ['a' , 'b' , 'c' , 'd']) #array for character 
c = array('d' , [1.25 , 3.25 , 4.66 , 9.99 ])
for i in a :
    print(i)
for i in b :
    print(i)
for i in c :
    print(i)    
array1 = array('i' , [1 ,2 , 3 , 4 , 5 ])
array2 = array(array1.typecode , (i*2 for i in array1))
for i in array2 :
    print(i)
#retrieving elements using array index 
from array import *
a = array('i' , [1 , 2, 3 , 4 ])
b = array(a.typecode , (i*8 for i in a))
length = len(a)
for i in range (length ):
    for j in range (i ):
        print("{} element is {}".format(i , b[j])) 
#
from array import *
i = 0 
a = array("i", [ ])
while i <= 10 :
    a.append(i)
    i += 1 
print(a)
print(a[1 : len(a): 2])
#array methods 
from array import *
array1 = array("i" , [ ])
i = 0
while i <= 100:
    if i % 2 == 0 :
        array1.append(i)
    i += 1
print(array1)
print(array1.count(5))
array1.extend(array("i" , [5 , 6 ]))
print(array1)
print(array1.pop())
#taking marks of 5 subjects as input printing total and percentage 
from array import *
arr1 = array("d" , [ ] )
sum1 = 0
subject_failed = 0 
for i in range(5):
    input1 = float(input("Enter your marks of your subject - {}  \t".format(i+1)))
    if input1 < 50 :
        subject_failed += 1
    sum1 += input1
    arr1.append(input1)
print("The total marks earned by you is {} \n You have failed in a total of {} subjects".format(sum1, subject_failed))
#bubble sort 
arr1 = array( "i",[ 1, 5 , 7 ,  3 , 2 ])
#descending order
print("Sequence in descending order ")
for i in range(len(arr1)):
    print ("Iteration {}".format(i+1))
    for j in range(i , len(arr1)):
        if arr1[i] < arr1[j]:
            temp = 0
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
        else:
            continue
    print(arr1)
#ascending order 
print(" \n Sequence in Ascending order ")
for i in range(len(arr1)):
    print ("Iteration {}".format(i+1))
    for j in range(i , len(arr1)):
        if arr1[j] < arr1[i]:
            temp = 0
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
        else:
            continue
    print(arr1)
#searching an element in an array 
arr1 = array("i",[85 , 45 , 22 , 15 , 75 ])
in1 = 0 
search = int(input("Enter an element to be searched for : \t "))
for i in range(len(arr1)) :    
    if search == arr1[i]:
        in1 += 1 
        print("The number is fount \n .It is located at position {}".format(i+1))
if in1 == 0 :
    print("Sorry not found")
#multi dimensional array
import numpy as np 
a = np.array([[1 , 32, 8 ],[5 , 8 , 9]])
print(a)
from numpy import *
a  =  array([[1 , 2 ],[3 , 4]], float)
print(a)
print(type(a[0][0]))
b = array([['a','b','c'],['d', 'e' , 'f']], dtype = char)
print(type(b[0][0]))
print(b)
from numpy import *
a = linspace( 0 , 100 )
print(len(a))
# comparing array 
from numpy import * 
a = array([[1 , 2 , 3 ],[4 , 5 , 6 ]])
b = array([[9 , 8 , 3 ],[ 3 , 10 , 22]])
c = a == b
print("Any one is true : " , any(c))
from numpy import * 
arr1 = array([1 , 2 , 3])
arr2 = array([5 , 
              8 , 
              9])
print(arr1)
print(type(arr1))
print(arr2)
print(type(arr2))
#retriving elements from a 2d array 
from numpy import *
a1 = array([[1 , 2 , 3 ], [4 , 5 , 6 ]])
print(a1)
for i in range(0 , 2):
    for j in range(0 , 3):
        print(a1[i][j])
from numpy import *
a1 = array([[1 , 2 , 3 , 4 , 5  ],[4 , 5 , 6 , 4 , 5 ],[7 , 8 , 9, 4 , 5 ]])
#performing slicing 
print(a1[0:3 , 0:3 ] )
from numpy import * 
arr1 = array([[1 , 2 , 3 ],[4 , 5 , 6 ],[7 ,8 , 9 ]])
a = matrix (arr1)
print(a)
print(diagonal(a))
print(a.max())
print(a.min())
print(a.sum())
print(a.mean())
m = matrix(arange(2,10).reshape(2,4))
print(m)
a = " hello \a world \b miketesting \r"
print(a)
#accesing eache elemnt of a string using indexing 
stri = "Hello welcome to python programming"
print("The length of the string is : {}".format(len(stri)) )
#forword -- using for loop
for i in range ( len(stri)):
    print(stri[i] , end = "")
#backword
print("\n")
for j in range(1, len(stri)+1):
    print(stri[-(j)] , end = "")
print("\n")
#forword using a while loop
i = 0
while i < len(stri):
    print(stri[i] , end = "")
    i += 1 
str1 = input("Enter your first string.")
str2 = "black" 
c = str1.find(str2 , 0 , len(str1))
if c == -1 :
    print("Sorry you have violated our guidelines ")
else:
    print("You are good to go ahead. ")
    print("Position of the string is {}".format(c))
str1 = input("Enter a sentence : \t ")
sub = "key"
i = 0 
while i < len(str1):
    a = str1.find( sub , i , len(str1))
    b = str1.count(sub)
    if a != -1:
        i = a + 1
        print("the string which you are searching i.e {} is located in the index {}".format( sub , a ))
    else:
        i += 1
print(b)
# to identify whitespaces, capitals, small letters , total letters in a sentence
str = input("Enter a string : ")
count = 0
whitespaces = 0
capitals = 0
smallletters = 0 
flag = False
storing_values = [ ]
for i in str:
    if i == " ": # for whitespacecs
        whitespaces += 1
    elif i.isupper():
        capitals += 1
        count += 1
    else:
        smallletters += 1
        count += 1
    storing_values.append(i)
words = 1
for i in range(len(str)-1):
    if storing_values[i] == " " and storing_values[i+1].isalpha :
        words += 1
print("Total Number of words : {}".format(words))
print("Total characters count : {} \n Total number of white spaces = {}".format(count, whitespaces))
print("Total capital letters : {}".format(capitals))
print("Total small letters : {}".format(smallletters))
print("Total number of words is : {}".format(whitespaces+1))

from array import *
def sum(arr1):
    """
    Parameters
    ----------
    arr1 : array with integrs as its parameters 
    Returns sum of array 
    ------
    """
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i]
    return sum
def oddoreven(arr1):
    """
    creating a method which finds out total number of odd and even 
    integers in the given array 
    """
    odd = 0
    even = 0
    for i in range(len(arr1)):
        if arr1[i]% 2 == 0 :
            even += 1 
        else:
            odd += 1
    return odd,even
arr1 = array("i", [ ])
j = int(input("Enter total number of subjects :"))
for i in range(j):
    a = int(input("Enter a number :{} ".format(i+1)))
    arr1.append(a)
print(sum(arr1))
o , e = oddoreven(arr1)
print("odd count is {} and even count is {}".format(o , e ))

#factorail 
def factorial(num):
    """ 
    finding the factorial of a given number 
    factorial of n = n * n-1 * n-2 *....1
    for example 4 =  4 *3*2*1
    """
    facto = 1 
    while num >= 1 :
        facto *= num
        num -= 1
    return facto
num = int(input("Enter a number : " ))
print(factorial(num))
#To check wether a number is prime or not 
def prime(a):
    """ 
    A number is called prime if it is divisible by only 1 and itself 
    example 2 .. 3.. 5..7
    """
    flag = 0
    for i in range(2 , a):
        if a % i == 0:
            flag += 1
    print(flag)
    if flag > 0 :
        print("Not a prime number ")
    else:
        print("A prime number ")
def set_of_prime_numbers(a):
    """ To generate a set of prime numbers """
    flag = 0
    for i in range(2 , 100):
        if a % i == 0:
            flag += 1
        else:
            print(i)
a = int(input("Enter a number : "))
prime(a)
b = int(input("Enter a number : "))
set_of_prime_numbers(b)
#recursive functions 
def recur(a):
    sum = 1
    if a == 0 :
        return sum 
    else:
        sum = a *recur(a-1)
        return sum
a = int(input("Enter a number : "))
print(recur(a))


#Tower of hanoi 
def hanoi( a , b , c):
    #step1 
    c.append(a[0])
    a.pop(0)
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))
    #step2
    for i in range(2,len(a)+1):    
        b.append(a[-i])
    for i in range(0 , len(a)-1):
        del a[: -1 : ]
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))
    #step 3 
    b.insert(0 , c[0])
    c.pop(0)
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))
    #step 4 
    c.append(a[0])
    a.pop(0)
    a.append(b[0])
    b.pop(0)
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))
    #step 5 
    for i in range(0 , len(b)):
        c.insert(0, b[i])
    for i in range(0 , len(b)-1):
        del b[:  : ]
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))
    #step 6 
    c.insert(0,a[0])
    del a[0]
    print(" A : {} \n B : {} \n C : {} \n ".format(a , b , c))    
a = [ ]
b = [ ]
c = [ ]
n = int(input("Enter number of disks :"))
for i in range(n):
    a.append(i+1)
hanoi(a , b , c )

#lambda function 
f = lambda x : a * a
a = int(input("Enter a number : "))
print(f(a))
f = lambda x , y ,z   : a + b + c
a , b , c = [int(i) for i in input("Enter two numbers with spaces").split(" ")]
print(f(a , b ,c))
#printing greatest number using lambda 
f = lambda a ,b : a if a > b else b
a , b = [int(x) for x in input("Enter two numbers : ").split(" ")]
f(a,b)
#bubble sort 
x = int(input("Enter the total number of elements in a list : ")) 
list1 = [ ]
for i in range(x): # taking values of list 
    list1.append(input("Enter number {} \t ".format(i+1)))
print(list1)
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
#selection sort
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
#insertion sort 
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
    
    
    

    
    
    
    
    
    



















