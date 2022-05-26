class student:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name        
    def appendsub(self,sub,dat):
        if self.name not in dat:
            dat[self.name]= set()
        dat[self.name].add(sub)
class subject:
    def __init__(self,name,code):
        self.subname=name        
        self.code=code
    def getsubname(self):
        return self.subname

data=dict()

English=subject("English","eng1012D")
Maths=subject("Maths","ma2021D")
Comp=subject("Computer Science","cs3120D")

sac=student("Sachin")
sac.appendsub(English.getsubname(),data)

cas=student("Cashin")
cas.appendsub(Maths.getsubname(),data)

sac.appendsub(Comp.getsubname(),data)
print(data)

def search(name):
    if name not in data:
        print("No student with such a name")
        return
    print(data[name])
search("Sachin")        
search("Aschin")
            
