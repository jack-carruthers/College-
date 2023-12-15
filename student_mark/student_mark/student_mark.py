# Jack Carruthers
# Student Marks 

file_path = "students.txt"
import sys
end = ("\n")

def adding_student(): # appending students 
    file = open(file_path, "a")
    stu_num = int(input("\n How many students would you like to input \n"))
    for x in range(stu_num):
        stu_info = input("\n Enter in format: \n Student full name / Student number / Marks \n")
        file.write(stu_info + "\n")
 
    
def review(): # See students and info
    file = open(file_path, "r")
    student_list = file.read()
    print(student_list)


def stop_func(): # Stop program
    exit_msg = input("\n Are you sure you want to exit? ( y / n ) \n")
    if exit_msg.lower() == "y": 
        stop_program()
    elif exit_msg.lower() == "n":
        print("Okay, returning back to program.")
    else:
        print("Invalid, please enter y or n (case sensitive)")
        

def stop_program():
    print("\n Exiting program...")
    sys.exit(0) # Searched exit command up on google
    

def search(): # Search for students in review, some google reference used
    serch = input("\n Enter student details to find \n")
    with open("C:\T-Level Digital Production\Library\student_mark\student_mark\students.txt", "r") as fp:
        for line_num, line in enumerate(fp):
            if (serch) in line:
                print("\n What you searched for is in database!")
                print("Line number:", line_num)
                print(line)
                
                break

  
def main():
    x = True 
    
    while x == True: 
        choice1 = int(input("\n Choose a function: \n Add Student info (1) \n Read Student info (2) \n Search Student info (3) \n Exit program (4)\n"))
        

        if choice1 == 1:
            x = False
            print(end)
            adding_student() 
            x = True
            
            
        if choice1 == 2:
            x = False
            print(end)
            review()
            x = True 
            
            
        if choice1 == 3:
            x = False 
            print(end)
            search()
            x = True 
            
        
        if choice1 == 4:
            x = False 
            print(end)
            stop_func()
            x = True
            
       


main() 
    
