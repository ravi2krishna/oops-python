from person import Person
from student import Student

class Trainer(Person):
    
    # Constructor with Non-static / Instance variables specific to each trainer
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile=None):
        Person.__init__(self, id=trainer_id, name=trainer_name, age=trainer_age, email=trainer_email, mobile=trainer_mobile)
        # NEWLY UPDATED 
        # Private trainer-specific state
        self.__total_sessions_taken = 0
        self.__payment_for_sessions = 0
        self.__training_bonus = 0
        self.__total_payment = 0

    # Non-static /Instance method: Calculate trainer payment 
    def sessions_payment(self):
        # NEWLY UPDATED 
        # Private trainer-specific state
        self.__total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 1500
        self.__payment_for_sessions = base_pay_per_session * self.__total_sessions_taken
        
        # Prompt for student's rating for the trainer (1 to 5):
        # If rating is 5 → add bonus of ₹5000
        # Otherwise → no bonus
        s1 = Student()
        print()
        print("=======Student Rating Given=======")
        # NEWLY UPDATED 
        # Private trainer-specific state
        self.__training_bonus = s1.trainer_ratings()
        self.__total_payment = self.__payment_for_sessions + self.__training_bonus
        print("=======Trainer Payment=======")
        print(f"Total Trainer Payment: {self.__total_payment}")
