class Student:
    
    # Static/class variables shared across all instances
    institute_name = "Edify"
    course_name = "Python"
    
    # Constructor with Non-static / Instance variables specific to each student
    # Student ID, Name, Age, Email & Mobile Number
    def __init__(self, student_id, student_name, student_age, student_email, student_mobile_number):
        # Instance variables specific to each student
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number
        
    # Class method : display institute info 
    @classmethod
    def institute_info(cls):
        print("="*50)
        print("Welcome To "+Student.institute_name)
        print("="*50)
        
    # Instance method: display basic student info => Hover Functionality 
    def student_basic_info(self):
        print("======= Basic Student Information =======")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
    
    # Instance method: display complete student info => Click Profile Functionality
    def student_complete_info(self):
        print("======= Basic Student Information =======")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Age: {self.student_age}")
        print(f"Student Email: {self.student_email}")
        print(f"Student Mobile No: {self.student_mobile_number}")        

    # Calculate sessions/attendance credits 
    def sessions_credits_cal(self):
        total_sessions_attended = 0
        attendance_credits = 0
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        if total_sessions_attended >= 30:
            attendance_credits = 5
        elif total_sessions_attended >= 20:
            attendance_credits += 3
        else:
            attendance_credits = 0
        return attendance_credits
    
    # NEWLY UPDATED
    # Calculate performance credits based on average score
    def performance_credits_cal(self, score):
        performance_credits = 0
        if score >= 85:
            performance_credits = 5
        elif score >= 60:
            performance_credits = 3
        else:
            performance_credits = 0
        return performance_credits

    # Calculate achievements (combines average score and session credits)
    def achievement_status(self):
        final_credits = 0
        # we can make this score_credits(90) dynamic also, will see next
        final_credits = self.performance_credits_cal(90) + self.sessions_credits()
        if final_credits >= 10:
            print("**** GOLD ****")
        elif final_credits >= 8:
            print("**** SILVER ****")
        else:
            print("**** BRONZE ****")
    
    # Calculate trainer rating bonus 
    def trainer_ratings(self):
        trainer_rating = int(input("Enter Trainer Rating: (1-5)"))
        if trainer_rating >= 5:
            return 5000
        else:
            return 0    