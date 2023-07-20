import random
number = random.randint(-10000, 10000)
conca1 = " and is greater than 5"
conca2 = " and is 0"
conca3 = " and is less than 6 and not 0"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last > 5:
    print("Last digit of {} is {}".format(number, last_digit) + conca1)
elif last == 0:
    print("Last digit of {} is {}".format(number, last_digit) + conca22)
else:
    print("Last digit of {} is {}".format(number, last_digit) + conca33)
