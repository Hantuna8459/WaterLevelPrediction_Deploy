from flask import Flask, render_template, request
from app.predicts import PredictForm, make_prediction
import logging

#logging.basicConfig(filename='app.log', level=logging.INFO) #debug mode, createa a log file

app = Flask(__name__)
app.config.from_object('config')
app.config['WTF_CSRF_ENABLED'] = False

# @app.route('/') 
# def hello_world(): 
#     return "Hello World"

@app.route('/', methods=['GET', 'POST'])

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        precipitation = form.precipitation.data
        sluice_status = form.sluice_status.data
        lag = form.lag.data
        
        # print data to log file
        # logging.info(f'precipitation: {precipitation}')
        # logging.info(f'sluice_status: {sluice_status}')
        # logging.info(f'lag: {lag}')
        
        prediction = make_prediction(precipitation, sluice_status, lag)
        return render_template('predict.html', prediction=prediction, form=form)
    return render_template('predict.html', form=form)
