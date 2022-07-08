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

    return """
    <html>
    <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
    </style>
    </head>
    <body>
    <div class="container">
    <table class="table">
    <tr>
        <th>User browser</th>
        <td>%s</td>
    </tr>
    <tr>
        <th>IP address</th>
        <td>%s</td>
    </tr>
     <tr>
        <th>Server time</th>
        <td>%s</td>
    </tr>
    </table>
    </div>
    </body>
    </html> 
    """ % (user_agent, ip_address, server_time)

@app.route("/source_code/")
def source_code():
    with open("app.py", "r") as f:
        result = f.read()

    result = result.replace('<', '&lt')

    return f'''
    <head>
        <title> Source code </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>

    </head>
    <body>
    <br> <br> <br>
    <div class="container-fluid d-flex align-items-center justify-content-center">
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
    Press for source code
    </button>
    </div>
    <div class="modal" id="myModal">
          <div class="modal-dialog">
            <div class="modal-content">
   
              <!-- Modal Header -->
              <div class="modal-header">
                <h4 class="modal-title">Source code Flask app</h4>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
              </div>
              <!-- Modal body -->
              <div class="modal-body"; style="white-space: pre">
                %s
              </div>
        
              <!-- Modal footer -->
              <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
    </div>
    </body>
     ''' % result

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

    return """
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>

    </head>
    <body>
    <br> <br> <br>
    <div class="container-fluid d-flex align-items-center justify-content-center">
    <button data-bs-toggle="collapse" data-bs-target="#demo">%s random symbols</button>
    </div>
    <div id="demo" class="collapse">
    <div class="container-fluid d-flex align-items-center justify-content-center">
    <p>%s</p>
    </div>
    </div>
    </body>
    """ % (length, ans_str)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')