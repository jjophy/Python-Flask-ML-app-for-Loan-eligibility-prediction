from flask import Blueprint,render_template,request
import pickle
import numpy as np
import sklearn

predict_view = Blueprint('prediction', __name__, template_folder="templates")
model = pickle.load(open('model.pkl', 'rb'))  # loading the trained model

@predict_view.route('/prediction.enter_details') ## for entering details
def enter_details():
    return render_template('predict.html')

@predict_view.route('/prediction.predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction==0:
        return render_template('predict.html', prediction_text='Sorry:( you are not eligible for the loan ')
    else:
        return render_template('predict.html', prediction_text='Congrats!! you are eligible for the loan')