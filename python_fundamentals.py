# A.Python is an indent based programming language
#The following program throws an indentation error. Correct it and make sure it prints properly.
import time

teams = ['Data', 'AI', 'DevOps']
for t in teams:
  print('Hello', t, 'Team from Inceptez Technologies')
  print('Keep Learning and Exploring!')


# B.Commented line in Python
#Use Case 1:
#Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.

#single-line
#number of students
students = 100
#number of trainers
trainers = 2
#sum of students and trainers
total = students + trainers
print(total)

#multi-line
"""calculate total number of students and trainers"""
students = 100
trainers = 2
total = students + trainers
print(total)

#Use Case 2:
#Convert the below block into a “dead code” using comments, then re-activate it later to print

#dead code print("Welcome to Inceptez Python Learning")

#C. Playing with Quotes
#Use Case 1:
#Create three string variables that correctly store and print:
#Use single, double, and triple quotes appropriately
#triple
"""This is Inceptez's "Python" class for Data Engineers & AI Engineers"""
#double
"This is Inceptez's" ' "Python"class for Data Engineers & AI Engineers'
#single


#Use Case 2:
#Write a multiline string using triple quotes that prints:

'''Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.'''

#D. Let's learn all about VARIABLES
#Use Case 1:
#Declare variables to store the following details:
Student_Name="kamalesh"
Course_Name="python fundamentals"
Training_Institute_Name="Inceptez Technologies"

#Then print a formatted message:
print(f"Name:{Student_Name} is learning the {Course_Name} at the institute{Training_Institute_Name}")

#Use Case 2:
#Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing character also by operating it with Eighteen percent gst

#dynamic inference
fee = 45000
print(type(fee))

#dynamic typing
fee = "45000"
print(type(fee))

#strongly typed
fee = 45000
gst = 18
total = fee + gst
print(total)

#E. Variables Naming Conventions
#Use Case 1:
#Identify which variable names below are invalid for Inceptez’s student database:

#invalid 2student = 'Ravi'
_student_id = 1001
studentName = 'Priya'
#invalid class name = 'Python'
incepte_batch = 'Morning'

#Use Case 2:
#Declare 3 variables following naming styles for Inceptez projects:

#PascalCase:
ProjectName="InceptezProjects"
#camelCase:
projectName="inceptezProjects"
#snake_case:
project_name="inceptez_projects"

#F. Type identification & Casting
#Use Case 1:
#Sample code: As we didn’t covered this function input() yet in our session, I am giving the below sample code for your reference.
#Write a program that asks for an employee’s age.
age="40"
#1. Checks its type is of string
print(type(age))
#2. Converts it to int (continue writing your program from here..)
age=40
print(type(age))
#3. Prints the years pending for retirement, for eg. 60 is the retirement age.
#Example:
#Enter your age: 40
#You will retire in 20 years at Inceptez Technologies.
age=40
retirement_age=60
years_pending_for_retirement= retirement_age-age
print(years_pending_for_retirement)

#Use Case 2 (Debug):
#Fix the type error in the following code for salary calculation:

salary = 50000
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

#G. Data types and casting
#Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
#Employee Salary Breakdown
#a. Write a program that asks the user for:
#employee_name (string)
employee_name="arun"
print(type(employee_name))
#base_salary (float)
base_salary=40000.0
print(type(base_salary))
#hra_percent (integer)
hra_percent=8000
print(type(hra_percent))
#bonus_amount (float)
bonus_amount=5000.0
print(type(bonus_amount))

#B. Convert inputs to the correct datatype if required.
#Calculate:
HRA = base_salary * (hra_percent / 100)
print(HRA)
Total_Salary = base_salary + HRA + bonus_amount
print(Total_Salary)

#C. Print the output like this:
employee_name="kamalesh"
print(employee_name)
base_salary: 40000.0
#HRA @ 20%: 8000.0
hra_percent=40000*20/100
print(hra_percent)
Bonus: 5000.0
#Total Salary Payable: ₹53000.0
total_salary = base_salary + bonus_amount + hra_percent
print(total_salary)







