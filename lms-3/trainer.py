from person import Person
from student import Student
# NEWLY UPDATED -> Trainer(Person) -> Inherit from Person Class
class Trainer(Person):
    
    # Constructor with Non-static / Instance variables specific to each trainer
    # NEWLY UPDATED -> id, name, age, email, mobile
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile=None):
        # NEWLY ADDED -> Calling Person Constructor
        Person.__init__(self, id=trainer_id, name=trainer_name, age=trainer_age, email=trainer_email, mobile=trainer_mobile)

    # Non-static /Instance method: Calculate trainer payment (interactive)
    def sessions_payment(self):
        self.total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 1500
        self.payment_for_sessions = base_pay_per_session * self.total_sessions_taken
        
        # Prompt for student's rating for the trainer (1 to 5):
        # If rating is 5 → add bonus of ₹5000
        # Otherwise → no bonus
        s1 = Student()
        print()
        print("=======Student Rating Given=======")
        self.training_bonus = s1.trainer_ratings()
        self.total_payment = self.payment_for_sessions + self.training_bonus
        print("=======Trainer Payment=======")
        print(f"Total Trainer Payment: {self.total_payment}")
