# Trainer Blueprint With Person Features
from person import Person
from student import Student

class Trainer(Person):
    
   # constructor with instance data 
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile_number=None):
        # Using Parent class constructor 
        Person.__init__(self,id=trainer_id,name=trainer_name,age=trainer_age,email=trainer_email,mobile_number=trainer_mobile_number)
        
    # instance method -> trainer payment calculation
    def trainer_payment_cal(self):
        total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 2000
        payment_for_sessions = total_sessions_taken * base_pay_per_session
        
        # get student rating 
        print("========= Student Rating Assigned =========")
        # bonus = trainer_rating_calculate()
        student = Student()
        bonus = student.trainer_rating_calculate()
        payment_for_sessions += bonus
        print("========= Trainer Payment To Be Made =========")
        print(f"Total Amount To Be Paid: {payment_for_sessions}")
         
        