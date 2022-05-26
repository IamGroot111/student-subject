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
print(sac.getname()) 
print(sac.getsub())
print(cas.deets())
sac.appendsub(Comp.getsubname())
print(sac.deets())
