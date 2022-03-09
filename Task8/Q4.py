import pandas as pd
sentense=""
size=int(input("enter the size of array:"))
element=[(input("enetr the element:"))
for i in range(size)]
s_element=pd.Series(element)
for i in range(len(element)):
    sentense+=(''+s_element[i])
print(sentense.title())    

