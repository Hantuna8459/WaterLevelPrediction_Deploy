from flask import Flask, request
from predict import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def prediction_route():
    return predict(request)

if __name__ == '__main__':
    app.run(debug=True)