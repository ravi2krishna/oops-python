class Student:
    
    # Static/class variables shared across all instances
    institute_name = "Edify"
    course_name = "Python"
    # NEWLY ADDED 
    global_discount = 0.1 # global site wide discount
    
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
    
    # NEWLY ADDED     
    # Instance method: calculate course fee with global discount and keywords
    def calculate_course_fee(self):
        discount = 0.0
        course_fee = 30000
        # if coupon is PROMO apply 5000 discount 
        # if coupon is FIFTY apply 15000 discount
        print("="*50)
        print("         COURSE FEE CALCULATION")
        print("="*50)
        student_coupon = input("Enter Coupon Code: ")
        if student_coupon == "PROMO":
            discount += 5000
        elif student_coupon == "FIFTY":
            discount += 15000

        # apply global discount
        gd = course_fee * Student.global_discount 

        final_fee = course_fee - (discount + gd) 

        print(f"Original Course Fee: ${course_fee}")
        print(f"Discount Applied Via Coupon: ${discount}") # Discount Applied Via Coupon
        print(f"Global Discount Applied: ${gd}")
        print(f"Final Course Fee after Discounts: ${final_fee}")       

    # Calculate sessions/attendance credits 
    def sessions_credits(self):
        print("="*50)
        print("         ATTENDANCE CALCULATION")
        print("="*50)
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        self.total_sessions_attended = total_sessions_attended
        if total_sessions_attended >= 30:
            self.attendance_credits += 5
        elif total_sessions_attended >= 20:
            self.attendance_credits += 3
        else:
            self.attendance_credits = 0
        return self.attendance_credits
    
    # NEWLY ADDED  
    # Get multiple scores dynamically and calculate average 
    def calculate_average_score(self):
        print("="*50)
        print("         AVERAGE SCORE CALCULATION")
        print("="*50)
        scores = []
        while True:
            score_input = input("Enter Score or type done: ")
            if score_input == "done":
                break
            if score_input.isdigit():
                score = int(score_input)
                if 0 <= score <=100:
                    scores.append(score)
                else:
                    print("Score Should be 0-100 ")
            else:
                print("Score Should Numbers Only")  
        
        average_score = sum(scores) / len(scores)
        return average_score
    
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
        # we can make this performance_credits(90) dynamic also
        # NEWLY UPDATED -> self.calculate_average_score()
        self.final_credits = self.performance_credits(self.calculate_average_score()) + self.sessions_credits()
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