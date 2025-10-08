# Parent Class with Common Attributes Of Student, Trainer & Future Entities
class Person:
    def __init__(self, id=None, name=None, age=None, email=None, mobile=None):
        # NEWLY UPDATED
        # Private attributes
        self.__id = id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__mobile = mobile

    # NEWLY ADDED 
    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    # mobile
    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        self.__mobile = value

    def person_complete_info(self):
        print("======= Complete Information =======")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile No: {self.mobile}")
