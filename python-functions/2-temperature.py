
# convert from fahrenheit to celsius

def convert_to_celsius(fahrenheit):
    celsius = (5/9 * (fahrenheit - 32))
    #ternicate so that it prints only two decimal places.
    if celsius < - 200:
        celsius = ("%0.2f" %celsius)
        return celsius
    else:
        return celsius


