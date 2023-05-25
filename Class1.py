import csv
class Table:
    def evaluate_sno(self,n,k):
        return 6*n+k+1
    def retrieve(self,FileName_):
        self.listofclasses=[]
        with open(FileName_,newline='')as f:
            reader=csv.DictReader(f)
            for row in reader:
                self.listofclasses.append(row)
        return self.listofclasses
    def specialretrieve(self,FileName_,k):
        x=self.retrieve(FileName_)
        self.checklist=[]
        for n_ in range(k,len(x),6):
            self.checklist.append(x[n_])
        return self.checklist
    def dict(self,FileName_):
        self.dictt={}
        f=open(FileName_,'r')
        x=f.readlines()
        for i in x:
            t=i.split(',')
            self.dictt[t[0]]=t[1]
        return self.dictt