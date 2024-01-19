from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, StopValidation
import pandas as pd
import joblib
import config

class PredictForm(FlaskForm):
    def validate_precipitation(form, field):
        if not field.data:
            raise StopValidation('Không được để trống')
        try:
            val = float(field.data)
            if val < 0:
                raise StopValidation('Lượng mưa phải là số dương')
        except ValueError:
            raise StopValidation('Lượng mưa phải là số')
    
    precipitation = StringField('precipitation', validators = [validate_precipitation])
    
    sluice_status = SelectField('sluice_status', choices = [('C', 'C'), ('S', 'S'), ('O', 'O'), ('O2', 'O2'), ('O1', 'O1'), ('L', 'L')],
        validators = [InputRequired(message='Hãy chọn trạng thái cống')]
        )
    def validate_lag(form, field):
        if not field.data:
            raise StopValidation('Không được để trống')
        try:
            val = float(field.data)
            if not 466 <= val <= 483:
                raise StopValidation('Mực nước hồ phải là số nằm trong khoảng 466 - 483(m)')
        except ValueError:
            raise StopValidation('Mực nước hồ phải là số')

    lag = StringField('lag', validators=[validate_lag])

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
    loaded_model = joblib.load(config.MODEL_PATH)
    prediction = loaded_model.predict(X_new)

    return prediction