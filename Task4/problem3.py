num=int(input("enter the no. of students\n"))
data=[["Roll No.","Name of Students","Marks"]]
for i in range(num):
    Roll=input("Enter the Roll No:")
    StudentsName=input("Enter the Students Name:")
    Marks=int(input("Enter the marks:"))
    data.append([Roll,StudentsName,Marks])
for i in range(len(data)):
    for j in range (len(data[i])):
        k=data[i][j]
        print(k,end='\t')
    print('\n')
R=int(input("enter the number of rows  to be printed:"))
for i in data[R]:
    print(i,end='\t')

