import random

number = random.randint(-10000, 10000)
number1= int(str(number)[-1])

if (number < 0):
     number1=-(number1)
if (number1 > 5):
    print("Last digit of {} is {} and is greater than 5".format(number,number1))
elif (number1 < 6 and number1 > 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,number1))
elif (number1 == 0):
    print("Last digit of {} is {} and is 0".format(number,number1))

