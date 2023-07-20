
# a function that checks a number is prime or not. 

def is_prime(number):
    count = 0
    for i in range (1 , number + 1):
        if (number % i == 0):
            count+=1
    if count == 2 or number == 2:
        return True
    else:
        return False

print(is_prime(0))
