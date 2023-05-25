from Class1 import Table
obj=Table()
n=input('Enter the Employee id')
d2={0:'mon',1:'tue',2:'wed',3:'thu',4:'fri',5:'sat'}
d3={'A':'9:40-10:40','B':'10:40-11:40','C':'11:40-12:40','D':'1:20-2:20','E':'2:20-3:20','F':'3:20-4:20'}
dictt=obj.dict('prof_data.csv')
d1={0:'cse-A',1:'cse-B',2:'cse-C'}
l=obj.retrieve('Data.csv')
c=0
k=0
for i in l:
    x=i.keys()
    for j in x:
        if(n in i[j]):
            print(dictt[n],'having class at',d3[j],'on ',d2[c%6],'slot',d1[k] )
    c+=1
    k=c//6