from this import d


x=int(input("enter the first number\n"))
y=int(input("enter the last number\n"))
r=""
s=". 0. 0. 0. 0. 0. "
for i in range(x,y):
    r=r+str(i)+s
print(r+str(y))
