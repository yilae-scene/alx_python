"""
a module that checks if the json response is correct or not.
"""
# import modules
import requests
import sys

# an aleady defined url
url = "http://0.0.0.0:5000/search_user"


if __name__== "__main__":
# work under dunder main to prevent the unwanted call-back 
    def checks_json(url):
        if len(sys.argv) >= 2:
            q = {"q": sys.argv[1]}
        elif len(sys.argv) == 1:
            q = ""
        r = requests.post(url, q)
        re = r.json()
        try:
            if len(re) == 0:
                print("No result")
            else:
                print("[{}],{}".format(re["id"], re["name"]))
        except Exception as e:
            print("Not a valid JSON")


checks_json(url)
