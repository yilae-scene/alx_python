
# a function that checks a number is prime or not. 

def is_prime(number):
    count = 0
    # itereat through to find it is evenly divided morethan twice and counter
    for i in range (1 , number + 1):
        if (number % i == 0):
            count+=1
    if count == 2 or number == 2:
        return True
    else:
        return False

