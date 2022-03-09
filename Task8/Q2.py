import numpy as np
array1=[]
a = int(input("size of array:\n"))
print("enter the elements of the array A")
for i in range(0,a):
    s=int(input())
    array1.append(s)


array2=[]

print("enter the elements of array B")
for i in range(0,a):
    s=int(input())
    array2.append(s)

    if array1==array2:
        print("True")
    else:
        print("false")    

