class Student:
    
    # Static/class variables shared across all instances
    institute_name = "Edify"
    course_name = "Python"
    
    # Constructor with Non-static / Instance variables specific to each student
    # Student ID, Name, Age, Email & Mobile Number
    def __init__(self, student_id=None, student_name=None, student_age=None, student_email=None, student_mobile_number=None):
        # Instance variables specific to each student
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number
        
        self.total_sessions_attended = 0
        self.attendance_credits = 0
        # NEWLY UPDATED
        self.performance_credit_points = 0
        self.final_credits = 0
        self.trainer_rating = 0
        
        
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
    def sessions_credits(self):
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        self.total_sessions_attended = total_sessions_attended
        if total_sessions_attended >= 30:
            self.attendance_credits += 5
        elif total_sessions_attended >= 20:
            self.attendance_credits += 3
        else:
            self.attendance_credits = 0
        return self.attendance_credits
    
    # NEWLY UPDATED
    # Calculate performance credits based on average score
    def performance_credits(self, score):
        if score >= 85:
            self.performance_credit_points += 5
        elif score >= 60:
            self.performance_credit_points += 3
        else:
            self.performance_credit_points = 0
        return self.performance_credit_points

    # Calculate achievements (combines average score and session credits)
    def achievement_status(self):
        # we can make this score_credits(90) dynamic also, will see next
        self.final_credits = self.performance_credits(90) + self.sessions_credits()
        if self.final_credits >= 10:
            print("**** GOLD ****")
        elif self.final_credits >= 8:
            print("**** SILVER ****")
        else:
            print("**** BRONZE ****")
    
    # Calculate trainer rating bonus 
    def trainer_ratings(self):
        self.trainer_rating = int(input("Enter Trainer Rating: (1-5)"))
        if self.trainer_rating >= 5:
            return 5000
        return 0    