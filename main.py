import time

print("Scanning the report")
time.sleep(3)
print("loading")
time.sleep(3)
print("Here is your report")

name = input("Name of the emp")
age = int(input("enter the age"))
building_number = input("enter the building number")
job_level = int(input("enter the job level"))
salary = int(input("enter the salary"))
location = input("enter the location")

if (job_level == 3 and salary <= 300000):
    print("Systems Enginner")
elif (job_level >= 4 and salary > 300000 ):
    print("techonlogy analyst")

print(f"Hi {name}")
print(f"your age is {age}")
if age > 30:
    print(f"Hi {name} you are senior employee")
elif age <= 30:
    print(f"Hi {name} you are a junior employee")

if (job_level == 3 and salary <= 300000):
    print("Systems Enginner")
elif (job_level >= 4 and salary > 300000 ):
    print("techonlogy analyst")

print(f"your prefered location is {location}")



