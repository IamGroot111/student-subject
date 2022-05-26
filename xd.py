class student:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def getsub(self):
        return self.subject
    def getname(self):
        return self.name        
    def appendsub(self,sub):
        self.subject.add(sub) 
    def deets(self):
        return self.name,self.subject
class subject:
    def __init__(self,name,code):
        self.subname=name        
        self.code=code
    def getsubname(self):
        return self.subname
English=subject("English","eng1012D")
Maths=subject("Maths","ma2021D")
Comp=subject("Computer Science","cs3120D")
sac=student("Sachin",{English.getsubname()})
cas=student("Cashin",{Maths.getsubname(),English.getsubname()})
data=dict()
data[sac.getname()]=sac.getsub()
data[cas.getname()]=cas.getsub()
print(sac.getname()) 
print(sac.getsub())
print(cas.deets())
sac.appendsub(Comp.getsubname())
print(sac.deets())
print(data)

def search(name):
    c=0   
    for names in data:
        if (names==name):
            print("The Subjects {} has enrolled in are:{}".format(name,data[name]))
            c=1
            break
    if(c==0):
        print("No student found with such a name")
search("Sachin")        
search("Aschin")
