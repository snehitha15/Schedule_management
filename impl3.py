from Class1 import Table
import json
obj=Table()
dictt=obj.dict('prof_data.csv')
d1={0:'cse-A',1:'cse-B',2:'cse-C'}
n=input('Enter Subject\n')
f1=open('data_f.txt','r')
x=f1.readlines()
f1.close()
list1=[]
for i in x:
  x1=i.replace("'", "\"")
  l=json.loads(str(x1))
  list1.append(l)
c=0
#list1=[{'1':'2','2':'2'},{'3':'2'}]
for i in list1:
    x=i.keys()
    for j in x:
        if(i[j]==n):
            print(dictt[j],'teaching for '+d1[c])
    c+=1