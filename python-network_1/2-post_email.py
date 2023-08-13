"""
takes a url and an email address as parameters and sends post request
"""
# import modules
import requests
import sys


def email_post(url, data):
    x = requests.post(url, data)
    po_x = x.text
    print(po_x)


if "__name__" == "__main__":
    # define a function

    if len(sys.argv) != 3:
        print("wrong number of arguments")

url = sys.argv[1]
data = {"email": sys.argv[2]}

email_post(url, data)
