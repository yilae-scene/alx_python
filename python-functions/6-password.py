
# here is a function that validates password.
def validate_password(password):
    #have the length of a string in variable
    length = len(password)
    # Have the conditions specified
    if (password.isupper() == False) == (password.islower() == False) and (length >= 8) and not(" " in password) and not(password.isalpha()):
        print (True)
    else:
        print(False)
 
validate_password("wllllllllllllllK2")

