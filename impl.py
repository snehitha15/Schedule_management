from Class1 import Table
import json
obj=Table()
dictt=obj.dict('prof_data.csv')
n=input("\nEnter the day (use 1st 3 small letters of the day) \n")
c=int(input("Enter the class\n"))
l=input("enter the slots\n").split()
#d1={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
#d1={"CSEA":0,"CSEB":1,"CSEC":2,"CSED":3,"CSEE":4,"CSEF":5}
d2={'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5}
x=obj.specialretrieve('Data.csv',d2[n])
ls=[]
for i in l:
    s=set()
    for j in x:
        s.update(j[i].split())
    ls.append(s)
set1=ls[0].union(*ls)
#print(set1)
list1=list(set1)
'''f1=open('staff.txt','r')
x=f1.readlines()
f1.close()
list1=[]
for i in x:
  x1=i.replace("'", "\"")
  l=json.loads(x1)
  list1.append(l)'''
for i in list1:
  print(dictt[i],'\n')
'''i=input('Enter 1 if you want for given sections else any other char' )
if(i=='1'):
  se=set(list1[c].keys())
else:
  se=set()
  for _ in list1:
    se.add(set(_.keys()))
print(se.difference(set1))'''