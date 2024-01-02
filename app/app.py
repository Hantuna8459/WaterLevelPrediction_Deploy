from flask import Flask, render_template, request
import pandas as pd
import joblib
import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        precipitation = request.form.get('precipitation')
        sluice_status = request.form.get('sluice_status')
        lag = request.form.get('lag')
        
        if not precipitation or not sluice_status or not lag:
            return render_template('index.html', error="Please fill in all fields")
        
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
        loaded_model = joblib.load(config.APP_ROOT + '/app/models/linear_regression.joblib')
        prediction=loaded_model.predict(X_new)

        return render_template('index.html', prediction=prediction)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)