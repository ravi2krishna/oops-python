# NEWLY UPDATED
from person import AbstractPerson
# NEWLY ADDED
from contracts import Payables
# SAME OLD
from student import Student

# NEWLY UPDATED -> Trainer(AbstractPerson) -> Inherit from AbstractPerson 
# and Payables 
class Trainer(AbstractPerson, Payables):
    
    # Constructor with Non-static / Instance variables specific to each trainer
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile=None):
        # NEWLY UPDATED AbstractPerson.__init__ earlier Person.__init__
        AbstractPerson.__init__(self, id=trainer_id, name=trainer_name, age=trainer_age, email=trainer_email, mobile=trainer_mobile)

    # Non-static /Instance method: Calculate trainer payment 
    def sessions_payment(self):
        # Private trainer-specific state
        total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 1500
        payment_for_sessions = base_pay_per_session * total_sessions_taken
        
        # Prompt for student's rating for the trainer (1 to 5):
        # If rating is 5 → add bonus of ₹5000
        # Otherwise → no bonus
        s1 = Student()
        print()
        print("=======Student Rating Given=======")
        # Private trainer-specific state
        training_bonus = s1.trainer_ratings()
        total_payment = payment_for_sessions + training_bonus
        print("=======Trainer Payment=======")
        print(f"Total Trainer Payment: {total_payment}")

    # NEWLY UPDATED 
    # Implementation of Payables interface
    def calculate_payment(self):
        """Calculate payment for the trainer (session payment)"""
        return self.sessions_payment()
