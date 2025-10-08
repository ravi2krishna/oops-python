# main logic and functionality 
from student import Student
from trainer import Trainer

def main():

    # Create a Student Instance with Basic Info => Click Profile Functionality
    # Student ID, Name, Age, Email & Mobile Number
    # NEWLY UPDATED -> Removed Old Hover Functionality
    s = Student(102, "Mike", 20, "mike@gmail.com", "9988776655")

    # Full Info Student
    # NEWLY ADDED -> Based On Object Call is done
    s.person_complete_info()

    # Calculate and Display Course Fee
    s.calculate_course_fee()
    
    # Student Achievements 
    s.achievement_status()

    # Create a Trainer Instance
    # NEWLY UPDATED -> Trainer with all details
    t = Trainer(901, "Ravi", 30, "ravi@gmail.com", "9999999999")

    # Display Trainer Info and Payment 
    # NEWLY ADDED -> Based On Object Call is done
    t.person_complete_info()
    t.sessions_payment()

main()