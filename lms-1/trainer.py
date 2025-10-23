from student import Student
class Trainer:
    
    # Constructor with Non-static / Instance variables specific to each trainer
    def __init__(self, trainer_id, trainer_name):
        # Instance variables
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name

    # Non-static / Instance method: Display trainer info
    def trainer_info(self):
        print("======= Trainer Information =======")
        print(f"Trainer ID: {self.trainer_id}")
        print(f"Trainer Name: {self.trainer_name}")

    # Non-static /Instance method: Calculate trainer payment (interactive)
    def sessions_payment(self,student):
        total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 1500
        payment_for_sessions = base_pay_per_session * total_sessions_taken
        
        # Prompt for student's rating for the trainer (1 to 5):
        # If rating is 5 → add bonus of ₹5000
        # Otherwise → no bonus
        print("=======Student Rating Given=======")
        training_bonus = student.trainer_ratings()
        total_payment = payment_for_sessions + training_bonus
        print("=======Trainer Payment=======")
        print(f"Total Trainer Payment: {total_payment}")
