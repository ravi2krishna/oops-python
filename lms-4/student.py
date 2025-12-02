from person import Person
# Student Blueprint With Person Features
class Student(Person):
    # class variables shared across all instances/objects of this class
    institute_name = "Edify"
    global_discount = 0.1 
    
    # constructor with instance data 
    def __init__(self, student_id=None, student_name=None, student_age=None, student_email=None, student_mobile_number=None):
        # Using Parent class constructor 
        Person.__init__(self,id=student_id,name=student_name,age=student_age,email=student_email,mobile_number=student_mobile_number)
    
    # class method -> display institute info 
    @classmethod
    def institute_info(cls):
        print("=" * 50)
        print("             Welcome To: "+Student.institute_name)
        print("=" * 50)
        
    # calculate sessions credits 
    def sessions_credits_cal(self):
        # local variables
        sessions_credits = 0
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        if total_sessions_attended >= 30:
            sessions_credits = 5
        elif total_sessions_attended >= 20:
            sessions_credits = 3
        else:
            sessions_credits = 0
        return sessions_credits
    
    # calculate score credits 
    def score_credits_cal(self,score):
        # local variables
        score_credits = 0
        if score >= 85:
            score_credits = 5
        elif score >= 60:
            score_credits = 3
        else:
            score_credits = 0
        return score_credits
    
    # calculate achievement status (combining sessions credits & score credits)
    def achievement_status(self):
        final_credits = self.sessions_credits_cal() + self.score_credits_cal(90)
        if final_credits >= 10:
            print("Got 🥇")
        elif final_credits >= 8:
            print("Got 🥈")
        else:
            print("Got 🥉")
    
    # give rating to trainer
    def trainer_rating_calculate(self):
        trainer_rating = int(input("Enter Trainer Rating (1-5): "))
        if trainer_rating >=5: 
            return 5000
        else:
            return 0
    
    # After 3 months New Functionality Added 
    # Calculate Course Fee Functionality 
    def course_fee_cal(self):
        coupon_discount = 0
        course_fee = 30000
        # if COUPON is "PROMO" give 5000 discount 
        # if COUPON is "FIFTY" give 15000 discount 
        print("=" * 50)
        print("             Course Fee Calculation")
        print("=" * 50)
        
        print(f"Original Fee: {course_fee}")
        # applying global discount
        gd = course_fee * Student.global_discount
        
        coupon = input("Enter Coupon Code: ")
        if coupon == "PROMO":
            coupon_discount = 5000
            course_fee -= coupon_discount
        elif coupon == "FIFTY":
            coupon_discount = 15000
            course_fee -= coupon_discount
        
        final_fee = course_fee - gd 
        
        print(f"Discount Through Coupon: {coupon_discount}")
        print(f"Discount Through Global: {gd}")
        print(f"Final Course Fee: {final_fee}") 