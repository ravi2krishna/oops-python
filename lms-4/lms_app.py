# Main Logic Calling 

from student import Student
from trainer import Trainer

def main():
    
    # For Student Click Functionality
    s2 = Student(102,"Mike",20,"mike@gmail.com",990909090)
    
    # Calling institute info 
    Student.institute_info()
    
    # Calling Student Complete Info
    s2.person_complete_info()
    
    # Calling Student Calculations Functionality
    s2.achievement_status()
    
    # Calling Student Course Fee Calculations Functionality
    s2.course_fee_cal()
    
    # For Trainer Hovering Functionality
    t1 = Trainer(200,"Ravi",30,"ravi2krishna@gmail.com",990909090)
    
    # Calling Trainer Complete Info
    t1.person_complete_info()
    
    # Calling Trainer Payment Functionality
    t1.trainer_payment_cal()

main()

    
    