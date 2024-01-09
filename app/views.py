from flask import Flask, request
from app.predicts import predict

app = Flask(__name__)

# @app.route('/') 
# def hello_world(): 
#     return "Hello World"

@app.route('/', methods=['GET', 'POST'])

@app.route('/predict', methods=['GET', 'POST'])
def prediction_route():
    return predict(request)

