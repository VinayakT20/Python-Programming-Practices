class thane():
    def __init__(self,name,rollno,subject):
        self.name = name
        self.rollno = rollno
        self.subject = subject

class mumbai(thane):
    def __init__(self,name,rollno,subject,age):
        super().__init__(name,rollno,subject)
        self.age = age

s1 = mumbai("vinayak",1,"python",18)
s2 = mumbai("vaidehee",2,"rprg",31)
s3 = mumbai("kranti",3,"sql",40)
s4 = mumbai("arvind",4,"html",25)

print(s2.subject)
print(s4.age)
