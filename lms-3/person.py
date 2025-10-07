# NEWLY ADDED
# Parent Class with Common Attributes Of Student, Trainer & Future Entities
class Person:
    def __init__(self, id=None, name=None, age=None, email=None, mobile=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile

    def person_complete_info(self):
        print("======= Complete Information =======")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile No: {self.mobile}")
