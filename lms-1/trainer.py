from student import Student
class Trainer:
    
    # Constructor with Non-static / Instance variables specific to each trainer
    def __init__(self, trainer_id, trainer_name):
        # Instance variables
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        self.total_sessions_taken = 0
        self.payment_for_sessions = 0
        self.training_bonus = 0
        self.total_payment = 0

    # Non-static / Instance method: Display trainer info
    def trainer_info(self):
        print("======= Trainer Information =======")
        print(f"Trainer ID: {self.trainer_id}")
        print(f"Trainer Name: {self.trainer_name}")

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
