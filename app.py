from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Cargo el modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_diabetes.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtengo los datos del formulario: las mismas características del dataset sobre diabetes
        age = float(request.form['age'])
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])

        features = np.array([[age, pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, diabetes_pedigree]])

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]

        result = {
            'prediction': int(prediction),
            'label': 'Diabético' if prediction == 1 else 'No diabético',
            'probability_positive': round(float(probability[1]) * 100, 1),
            'probability_negative': round(float(probability[0]) * 100, 1),
        }
        
        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
