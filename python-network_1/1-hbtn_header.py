""" 
this is a module that use the modules of 'requests' and 'sys' to employ request and CLI arguments
"""
import requests
import sys

if __name__ == "__main__":
    
    # define a function
    
    def request_x(url):
        """ 
        define a function that takes a url from the CLI and returns the X-request
        """
        if len(sys.argv) == 2:
            # try and except to makes sure that right argument is made
            try:
                r = requests.get(url)
                x = r.headers['X-Request-Id']
                return x
            except Exception as e:
                print(e)
        else:
            if len(sys.argv) != 2:
                print('inproper number of CLI arguments')
 
url = sys.argv[1]
new_x = request_x(url)
if new_x:
    print(new_x)
else:
    print("None")
