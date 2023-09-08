# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request


# creating a Flask app
app = Flask(__name__)


# Get and Post, Returning hello world if you navigate to the root
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
    

# Calculate the Square root of a number
# http://127.0.0.1:5000 / squareroute / 10
@app.route('/squareroute/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})
    

# main function
if __name__ == '__main__':
  
    app.run(debug = True)