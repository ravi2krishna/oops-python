from contracts import Personable, Payables

# Abstract base class for common person attributes and methods
class AbstractPerson(Personable):
    def __init__(self, id=None, name=None, age=None, email=None, mobile=None):
        # Private attributes
        self.__id = id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__mobile = mobile

    # Properties for encapsulated access
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, value):
        self.__mobile = value

    # NEWLY ADDED 
    # Implementation of Personable interface
    def set_personal_details(self, id, name, age, email, mobile):
        """Set personal details for the entity"""
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile

    def person_complete_info(self):
        """Display complete personal information"""
        print("======= Complete Information =======")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile No: {self.mobile}")
 