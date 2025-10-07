# main logic and functionality 
from student import Student
from trainer import Trainer

def main():

    # Create a Student Instance with Basic Info => Hover Functionality 
    s1 = Student(101, "John")
    
    # Create a Student Instance with Basic Info => Click Profile Functionality
    # Student ID, Name, Age, Email & Mobile Number
    s2 = Student(102, "Mike", 20, "mike@gmail.com", "9988776655")

    # Display Student Info
    s1.student_basic_info()

    # Full Info Student
    s2.student_complete_info()

    # Student Achievements 
    s1.achievement_status()

    # Create a Trainer Instance
    t1 = Trainer(901, "Ravi")

    # Display Trainer Info and Payment (interactive)
    t1.trainer_info()
    t1.sessions_payment()

main()