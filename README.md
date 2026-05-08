# 🩺 DiabetesScan: Predicción de diabetes usando Flask + Random Forest
Se trata de una aplicación web que predice el riesgo de diabetes. Usa un modelo de Machine Learning (Random Forest) entrenado con el conjunto de datos Pima Indians Diabetes Dataset del Instituto Nacional de Diabetes y Enfermedades Digestivas y Renales.

🔗 **Demo en vivo**: [enlace-a-render-aqui]

---

## 📁 Estructura del proyecto

```
diabetes-flask/
├── app.py # Aplicación Flask principal
├── Procfile # Configuración para Render
├── requirements.txt # Dependencias Python
├── save_model.py # Script para exportar el modelo desde el notebook
├── models/
│   └── random_forest_diabetes.pkl # Modelo entrenado
└── templates/
    └── index.html # Interfaz web
```

---

## 🚀 Instalación local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Tener el modelo en models/random_forest_diabetes.pkl

# 3. Ejecutar
python app.py
```

Abrir http://localhost:5000

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
