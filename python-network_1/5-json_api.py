"""
a module that checks if the json response is correct or not.
"""
# import modules
import requests
import sys

# an aleady defined url


def checks_json(q):
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, q)
    return r
if __name__ == "__main__":
    # work under dunder main to prevent the unwanted call-back
        if len(sys.argv) >= 2:
            q = {"q": sys.argv[1]}
        elif len(sys.argv) == 1:
            q = ""
        r = checks_json(q)
        re = r.json()
        try:
            if len(re) == 0:
                print("No result")
            else:
                print("[{}] {}".format(re["id"], re["name"]))
        except ValueError:
            print("Not a valid JSON")


checks_json(url)
