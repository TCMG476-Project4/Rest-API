from flask import Flask, jsonify, abort, make_response, request
from urllib import request as urlRequest
import hashlib
import math
import json
from slackclient import SlackClient


app = Flask(__name__)


@app.errorhandler(404) #Handles 404 errors
def notFound(error):
    return make_response(jsonify({'error': '404: Page not found.'}), 404)


@app.route('/md5/<string:string>', methods=['GET']) #MD5
def getMD5(string):
    md5Hash = hashlib.md5(str(string).encode('utf-8')).hexdigest()
    return jsonify({'input':string, 'output':md5Hash})


@app.route('/is-prime/<int:x>', methods=['GET']) #Prime
def getprime(x):
    if x == 1:
        return jsonify({'input':x, 'output':False})

    for number in range(2,int(x**0.5)+1):
            if x%number==0:
                a = False
                return jsonify({'input':x, 'output':a})
    a = True
    return jsonify({'input':x, 'output':a})

@app.route('/factorial/<int:x>', methods=['GET']) #Factorials
def getFactorial(x):
    factorial = math.factorial(int(x))
    return jsonify({'input':x, 'output':factorial})

@app.route('/slack-alert/<string:string>', methods=['GET']) #Slack-Alert
def slackPost(string):
    post = {"text": "{0}".format(string)}

    json_post = json.dumps(post)
    req = urlRequest.Request("https://hooks.slack.com/services/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", data = json_post.encode('ascii'), headers = {'Content-Type': 'application/json'})
    urlRequest.urlopen(req)
    return jsonify({'input':string, 'output':True})

@app.route('/fibonacci/<int:x>', methods=['GET']) #Fibonacci
def fibonacci(x):
    if x >= 0:
        a = 0
        b = 1
        fibArray = [a,b]
        
        while b <= x:
            a,b = b, a+b
            fibArray.append(b)
        
        fibArray = fibArray[:-1]
    else:
        b = "You need to choose a number greater than 0"
        fibArray = []
        fibArray.append(b)
    return jsonify({'input':x, 'output':fibArray})

#400 error for an invalid input
@app.route('/fibonacci/<string:inStr>', methods=['GET'])
def fibErr(inStr):
    return make_response(jsonify({'error': '400: Invalid Input'}), 400)
@app.route('/factorial/<string:inStr>', methods=['GET'])
def factErr(inStr):
    return make_response(jsonify({'error': '400: Invalid Input'}), 400)
@app.route('/is-prime/<string:inStr>', methods=['GET'])
def primeErr(inStr):
    return make_response(jsonify({'error': '400: Invalid Input'}), 400)

if __name__ == "__main__":
    app.run(host="0.0.0.0") 
