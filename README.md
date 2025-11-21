# SmartDiab: A Diabetes Prediction System

SmartDiab is a machine learning-based web application that predicts the likelihood of diabetes using key health parameters. The project uses **Python**, **Scikit-Learn**, and **Streamlit** to deliver an easy-to-use, interactive interface.

---

## 🌍 Live Demo  
🔗 **Public URL:** [https://smartdiab.streamlit.app/](https://smartdiab-wkwidxfpbttxv67p2m5ek5.streamlit.app/)

---


## 🚀 Features
- Predicts diabetes risk using ML models  
- Clean and user-friendly Streamlit interface  
- Real-time input form for health parameters  
- Trained on the standard PIMA Diabetes Dataset  
- Modular and easy-to-understand project structure  

---

## 📁 Project Structure

SmartDiab/


│
├── app.py            # Streamlit app

├── model.pkl         # Trained ML model

├── diabetes.csv      # Dataset (optional)

├── requirements.txt  # Dependencies

└── README.md         # Documentation


---

## 🧠 Machine Learning Model
- **Algorithm:** Random Forest Classifier (or your selected model)  
- **Dataset:** PIMA Diabetes Dataset  
- **Preprocessing:** Scaling using StandardScaler  

Model predicts:  
👉 **0 — No Diabetes**  
👉 **1 — Diabetes**

---

## 🖥️ How to Run the Project Locally

### **1. Clone the Repository**

```bash
git clone https://github.com/vanshgupta74SmartDiab.git
cd SmartDiab
```
> This command downloads the project and moves into the folder.

 #### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```
> This command installs every dependency needed to run the project, exactly as listed in requirements.txt.

### **3. Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 📊 Input Features
SmartDiab uses these health parameters:

- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin Level  
- BMI  
- Diabetes Pedigree Function  
- Age  

---

## 🌐 Deployment Options
You can deploy on:

- Streamlit Cloud  
- Render  
- Railway  

---

## 🧩 Requirements

- pandas
- numpy
- scikit-learn
- streamlit


---

## 🤝 Contributing
Pull requests are welcome.  
For major changes, please open an issue first.

---

## 📜 License
Open-source under the **MIT License**.

---

## ❤️ Acknowledgments
- PIMA Diabetes Dataset  
- Streamlit team  
- Scikit-Learn community  
