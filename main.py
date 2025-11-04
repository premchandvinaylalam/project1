import time

print("Scanning the report")
time.sleep(3)
print("loading")
time.sleep(3)
print("Here is your report")

name = input("Name of the emp")
firstname = input("enter the first_name")
last_name = input("enter the last_name")
age = int(input("enter the age"))
project = input("enter the project name")
job_level = int(input("enter the job level"))
salary = int(input("enter the salary"))
location = input("enter the location")
username = firstname[0:3]+last_name[0:2]+str(age)[-1]

if (job_level == 3 and salary <= 300000):
    job_tag = "Systems Enginner"
elif (job_level >= 4 and salary > 300000 ):
    job_tag = "techonlogy analyst"

if project == "apple":
    bulid_tag = "building 8"
elif project == "Broadcom":
    bulid_tag = "building 9"
else:
    bulid_tag = "you need to work from common building 1-3"

print(f"Hi {name}")
print(f"your age is {age}")
if age > 30:
    print(f"Hi {name} you are senior employee")
elif age <= 30:
    print(f"Hi {name} you are a junior employee")
print("="*60)
print(f"your designation is {job_tag}")
print(f"your prefered location is {location}")
print(f"your email address is {username}@infosys.com")
print(f"your building number is {bulid_tag}")





