from flask import Flask, render_template, request
from predict import make_prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        precipitation = request.form.get('precipitation')
        sluice_status = request.form.get('sluice_status')
        lag = request.form.get('lag')
        
        # if not precipitation or not sluice_status or not lag:
        #     return render_template('index.html', error="Please fill in all fields")
        
        prediction = make_prediction(precipitation, sluice_status, lag)
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)