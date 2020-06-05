import requests

def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_request('http://www.ustack.com')
