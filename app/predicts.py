from flask import render_template
import pandas as pd
import joblib

def make_prediction(precipitation, sluice_status, lag):
    status_mapping = {
        'C': 0,
        'S': 1,
        'O': 2,
        'O2': 3,
        'O1': 4,
        'L': 5
    }
    
    sluice_status = status_mapping.get(sluice_status)

    X_new = pd.DataFrame({'precipitation': [precipitation], 'sluice_status': [sluice_status], 'lag': [lag]})
    loaded_model = joblib.load('machine_learning_model/linear_regression.joblib')
    prediction = loaded_model.predict(X_new)

    return prediction

def predict(request):
    if request.method == 'POST':
        precipitation = request.form.get('precipitation')
        sluice_status = request.form.get('sluice_status')
        lag = request.form.get('lag')
        
        prediction = make_prediction(precipitation, sluice_status, lag)
        return render_template('predict.html', prediction=prediction)
    return render_template('predict.html')