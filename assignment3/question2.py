# Question2


class Staff:
    name:str
    subject:str
    post:str
    def __init__(self,name,subject,post):
        self.name=name
        self.subject=subject
        self.post=post

class Teacher(Staff):
    def __init__(self, name, subject, post):
        super().__init__(name, subject, post)

    def get(self):
        print(f"{self.name} teacher who takes {self.subject} subject is our {self.post} staff")


obj=Teacher("Reena","maths","permanent")
obj.get()