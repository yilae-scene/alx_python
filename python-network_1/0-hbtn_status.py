"""
    this is a script that uses that request module to
    request and get the text back 
"""
import requests # import request

if __name__ == "__main__":
    r = requests.get('https://alu-intranet.hbtn.io/status') 
    print('Body response:')
    print('\t-type: {}'.format(type(r.text)))
    print('\t-content: {}'.format(r.text))
