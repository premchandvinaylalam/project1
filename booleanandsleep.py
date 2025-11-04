'''Boolean -- (true and False)
It will check value is true or false print the results'''

webscarp = True
if webscarp == True:
    print("success")
else:
    print("false")

'''sleep method --- When we use sleep method particular line of code wait for the time we have mentioned
import time
and write the code (time.sleep(default value is seconds))'''

import time

print("data is processing")

time.sleep(3)  #--- above line will executes and wait for 3 seconds

print("Data is loading")

time.sleep(5) #-- it will wait for 5 seconds


#TO KNOW THE EXECUTION TIME OF CODE (EX:How much time code is taking to execute)
#use time.time

import time

t1 = time.time()

print("data is successfully loaded")

time.sleep(6)

t2 = time.time()

print(t2-t1)  # -- To know the execution time