import math
import random

x = random.randint(1,10)
con = 2
count = 0

while(1):
    count = count + 1
    test = int(input('Enter a no.'))

    if test == x:
        
        print('You WIN\nGuessed Correctly in',count)
        break
    elif math.fabs(test-x) <= con:
        print('you are close to ANSWER')
    else:
        print('You are far from ANSWER')
    