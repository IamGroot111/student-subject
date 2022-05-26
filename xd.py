class student:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def getsub(self):
        return self.subject
    def getname(self):
        return self.name        
class subject:
    def __init__(self,name,code):
        self.subname=name        
        self.code=code
    def getsubname(self):
        return self.subname
English=subject("English","eng1012D")
Maths=subject("Maths","ma2021D")
Comp=subject("Computer Science","cs3120D")
sac=student("Sachin",{English.getsubname(),Comp.getsubname()})
cas=student("Cashin",{Maths.getsubname(),English.getsubname()})
asc=student("Aschin",{English.getsubname(),Maths.getsubname()})
sca=student("Scahin",{English.getsubname(),Maths.getsubname(),Comp.getsubname()})
print(sac.getname())
print(sac.getsub())
print(cas.getname())
print(cas.getsub())
print(asc.getname())
print(asc.getsub())
print(sca.getname())
print(sca.getsub())
