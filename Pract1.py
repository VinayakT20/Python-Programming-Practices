class myclass:
    course = "Data Science"
    def __init__(self,subject,roll,name):
        self.subject=subject
        self.roll=roll
        self.name=name

sybsc1 = myclass("python",41,"Vinayak")
sybsc2 = myclass("r",24,"Shravani")
sybsc3 = myclass("html",14,"Kshitij")

print(sybsc1.roll)
print(sybsc3.subject)
print(sybsc2.name)
print(sybsc1.name)

