"""
this displays the error message with status_code
"""
# import modules
import requests
import sys

if __name__ == "__main__":
    # define the def that prints Error message
    def err_mess(url):
        r = requests.get(url)
        err = r.status_code
        if err >= 400:
            print("Error code: {}".format(err))
        else:
            #print the body
            print(r.text)
url = sys.argv[1]
err_mess(url)
