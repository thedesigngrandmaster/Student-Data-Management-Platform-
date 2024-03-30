import tabulate

class Student:
    def student_details(self, name, matric_number, gpa, scholarship_eligibility):
        self.name = name
        self.matric_number = matric_number
        self.gpa = gpa
        self.scholarship_eligibility = scholarship_eligibility

    def calculate_average_GPA(self, gpa):
        self.gpa = gpa
        return self.gpa
    
    def print_STUDENT_DETAILS(self):
        print(f"Name: {self.name}\nMatric Number: {self.matric_number}\nGPA: {self.gpa}\nScholarship Eligibility: {self.scholarship_eligibility}")

    def check_scholarship_eligibility(self):
        gpa_float = float(self.gpa)
        if gpa_float >= 4.75:
            self.scholarship_eligibility = "You're Eligible for the CSC Scholarship Programme"
        else:
            self.scholarship_eligibility = "Sorry! You're NOT Eligible for the CSC Scholarship Programme"

            print(self.scholarship_eligibility)

"""Create a new student object. This object will have/inherit the attributes of the class Student"""        
student = Student()

"""We are going to get the student information from the user"""
print("Welcome to CSC Students Management Platform.\nPlease enter your details below to know if you are eligible for the CSC Scholarship Programme.")        
name = input("Your Full Name e.g \"John Doe\": ")
matric_number = input("Your Matric. Number e.g \"230591042\": ")
gpa = input("Your 1ST SEMESTER GPA: ")

"""Now, we are going to set the student attributes"""
student.student_details(name, matric_number, gpa, None)

"""We'll calculate the average GPA and check the scholarship eligibility"""
student.calculate_average_GPA(gpa)
student.check_scholarship_eligibility()

"""Print the student details"""
student.print_STUDENT_DETAILS()

"""Now, we are going to create atable to enter the data (or student informations)"""
table_header = ["Name", "Matric number", "GPA"]

table_body = [[student.name, student.matric_number, student.gpa]]

print(tabulate.tabulate(table_body, headers = table_header, tablefmt="grid"))