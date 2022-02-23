# This program will check if the given number is a palindrome number.

num=int(input("Enter the number\n"))
rev=0
x=num
while(num>0): 
    rev=(rev*10)+num%10 # This will find the reverse of the given number
    num=num//10

if(x==rev):
     print("True")

else:
    print("False");



