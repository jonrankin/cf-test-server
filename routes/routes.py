from flask import Flask, request, jsonify, make_response, render_template
import json
import requests

app = Flask(__name__, template_folder='../templates')

#load in status codes
with open('static/json/status_codes.json') as code_file:
     status_codes = dict(json.load(code_file))


@app.route("/status/<code>", methods = ['GET', 'POST', 'PUT'])
def index(code):
   if code in status_codes:
      return render_template('error.html',error_code = code, error_message = status_codes[code]["message"], img_src= "../static/img/" + status_codes[code]["image"]),int(code)
   return make_response("Not a Supported Code",404)

if __name__ == "__main__":


     #requests.get('http://www.ietf.org/assignments/http-status-codes/http-status-codes-1.csv')
     app.run(host='0.0.0.0')

