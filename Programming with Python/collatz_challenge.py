# Author: Yasin Aydas
# Date Created: 11.11.2024
# Last modified: 11.11.2024
# Description: Collatz Challenge algorithm

# starting at 27
number = 27
steps = 0

for i in range(200):
    if number == 1: # when you reach 1, stop
        break
    # fill in the rest of this program
    number = number // 2 if number % 2 == 0 else (number * 3 + 1)
    steps += 1

    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")