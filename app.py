from flask import Flask, request, render_template, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to store data in session
model = joblib.load('svm_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    bmi = float(request.form['bmi'])
    skin_thickness = float(request.form['skin_thickness'])

    input_data = np.array([[age, bmi, skin_thickness]])
    prediction = model.predict(input_data)[0]

    # Save prediction in session
    session['prediction'] = int(prediction)

    # Redirect to result page
    return redirect(url_for('result'))

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_result = None
    category = None
    if request.method == 'POST':
        height = float(request.form['height']) / 100  # cm to meters
        weight = float(request.form['weight'])
        bmi_result = round(weight / (height * height), 2)

        if bmi_result < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_result < 24.9:
            category = "Normal weight"
        elif 25 <= bmi_result < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

    return render_template('bmi.html', bmi_result=bmi_result, category=category)

@app.route('/result')
def result():
    prediction = session.get('prediction', None)
    if prediction is None:
        return redirect(url_for('home'))  # If no prediction, go back home

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
