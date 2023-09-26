# Be properly commented
# Contain at least 1 example of error handling 
# Contain at least 1 example of data validation on an input
# Use both a for loop & a while loop
# Be submitted in the correct folder on GitHub.

import shutil
import time

#loop
while True:
  #try except to validate datatype
    try:
        for i in range(3):
            number = int(input("Enter 2007 3 times or else: "))
          #checks if number is not 2007
            if number != 2007:
                os.system('shutdown /s /t 0')
        break
    except ValueError:
      #adds except condition
        os.system('shutdown /s /t 0')

print("congratulations, your computer didn't shut down")
time.sleep(3)
os.system('shutdown /s /t 0')
