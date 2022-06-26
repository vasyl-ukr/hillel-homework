import string
import time
import random

from flask import Flask, request


app = Flask(__name__)
app.debug = True

@app.route("/whoami/")
def whoami():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    server_time = time.strftime('%A %B, %d %Y %H:%M:%S')

    return f"""
    <h3/> User browser: {user_agent} </h3> 
    <h3/> IP_address: {ip_address} </h3>
    <h3/> Server time: {server_time} </h3>
    """

@app.route("/source_code/")
def source_cod():
    pass

@app.route("/random/")
def home():

    length = int(request.values.get('length', ''))
    specials = request.values.get('specials', '')
    digits = request.values.get('digits', '')

    letters = string.ascii_letters

    if specials == "1":
        letters += '!"№;%:?*()_+.'
    if digits == "1":
        letters += string.digits

    ans_str = ''.join(random.choice(letters) for i in range(length))

    return ans_str

if __name__ == 'main':
    app.run(use_reloader=True)



