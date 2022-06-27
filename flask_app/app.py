import string
import time
import random

from flask import Flask, request


app = Flask(__name__)

@app.route("/whoami/")
def whoami():
    user_agent = request.headers.get('User-Agent', '')
    ip_address = request.remote_addr
    server_time = time.strftime('%A %B, %d %Y %H:%M:%S')

    return f"""
    <head>
        <title> User info </title>
    </head>
    <body>
        <p> User browser: {user_agent} </p>
        <p> IP_address: {ip_address} </p>
        <p> Server time: {server_time} </p>
    </body>
    """

@app.route("/source_code/")
def source_code():
    with open("app.py", "r") as f:
        result = f.readlines()

    result = [lines + '<br>' for lines in result]

    result = ''.join(result)

    return f'''
    <head>
        <title> Source code </title>
    </head>
    <body>
        
        {result}
     </body>
     '''



@app.route("/random/")
def random_string():

    length = request.values.get('length', '')
    specials = request.values.get('specials', '')
    digits = request.values.get('digits', '')

    check_length = [str(i) for i in range(1, 101)]
    check_bool = ['', '0', '1']

    if not (length in check_length and specials in check_bool and digits in check_bool):
        return "Not valid request"

    symbols = string.ascii_letters

    if specials == "1":
        symbols += '!"№;%:?*()_+.'
    if digits == "1":
        symbols += string.digits

    ans_str = ''.join(random.choice(symbols) for i in range(int(length)))

    return ans_str
