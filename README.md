# 🩺 DiabetesScan: Predicción de diabetes con Flask + Random Forest
Se trata de una aplicación web que predice el riesgo de diabetes. Usa un modelo de Machine Learning (Random Forest) entrenado con el conjunto de datos Pima Indians Diabetes Dataset del Instituto Nacional de Diabetes y Enfermedades Digestivas y Renales.

🔗 **Demo en vivo**: [enlace-a-render-aqui]

---

## 📁 Estructura del proyecto

```
App-web-de-ML-usando-Flask/
├── models/
│   └── random_forest_diabetes.pkl # Modelo entrenado
└── templates/
    └── index.html # Interfaz web
├── Procfile # Configuración para Render
├── README.md
├── app.py # Aplicación Flask principal
├── requirements.txt # Dependencias Python
```

---

## 🚀 Instalación local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Tener el modelo guardado en models/random_forest_diabetes.pkl

# 3. Ejecutar
python app.py
```

Abrir Localhost

---

## 🤖 Modelo
- **Algoritmo**: Random Forest Classifier
- **Dataset**: Pima Indians Diabetes (Kaggle)
- **Features**: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- **Target**: 0 (no diabético) / 1 (diabético)

---

## ☁️ Deploy en Render
1. Subir este proyecto a GitHub
2. Ir a [render.com](https://render.com) ->- New --> Web Service
3. Conectar el repositorio
4. Configurar:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn app:app`
   - **Plan**: Free
5. Hacer click en **Deploy**

---

## ⚠️ Aviso
Este modelo es orientativo y no reemplaza un diagnóstico médico profesional.
