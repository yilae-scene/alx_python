"""
authenticat an git api with a username and token as passwords that are passed as an arguments in CLI
"""
# import modules
import requests
import sys




if __name__ == "__main__":
        url = 'https://api.github.com/user'
        request = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
        re = request.json()
        print(re.get("id", "None"))

