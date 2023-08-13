"""
a module that checks if the json response is correct or not.
"""
# import modules
import requests
import sys

# an aleady defined url


def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    return response


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No result")
        sys.exit(1)

    letter = sys.argv[1]

    response = search_user(letter)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")
