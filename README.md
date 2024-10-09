# Blood Cell Analysis ( Anemia Type ) Prediction (ML Classification Project)

## Blood Cell Analysis ( Anemia Type ) Prediction Project Documentation

### Table of Contents
1. Introduction  
2. Dataset Description  
3. Project Objectives  
4. Project Structure  
5. Data Ingestion  
6. Data Transformation  
7. Model Training  
8. Training Pipeline  
9. Prediction Pipeline  
10. Flask (Web Interface)  
11. Logging  
12. Exception Handling  
13. Utils  
14. Conclusion  

### 1. Introduction  
The Blood Cell Analysis Prediction project aims to classify patients based on various blood test results to predict certain medical conditions. This document outlines the project structure, processes, and supporting scripts that power the model's predictions.

### 2. Dataset Description  
**Dataset Name:** Blood Cell Analysis Dataset  

**Description:**  
The dataset contains 1,281 entries with 15 columns, capturing blood cell analysis data used to predict a patient’s diagnosis. Below is a brief description of each column:

- **WBC:** White Blood Cell count (float)
- **LYMp:** Lymphocyte percentage (float)
- **NEUTp:** Neutrophil percentage (float)
- **LYMn:** Lymphocyte number (float)
- **NEUTn:** Neutrophil number (float)
- **RBC:** Red Blood Cell count (float)
- **HGB:** Hemoglobin concentration (float)
- **HCT:** Hematocrit level (float)
- **MCV:** Mean Corpuscular Volume (float)
- **MCH:** Mean Corpuscular Hemoglobin (float)
- **MCHC:** Mean Corpuscular Hemoglobin Concentration (float)
- **PLT:** Platelet count (float)
- **PDW:** Platelet Distribution Width (float)
- **PCT:** Plateletcrit (float)
- **Diagnosis:** Target column (whether the patient has a specific diagnosis, object)

### 3. Project Objectives  
- **Data Ingestion:** Load and explore the blood cell analysis dataset.
- **Data Transformation:** Clean, preprocess, and transform the dataset for model analysis.
- **Model Training:** Train machine learning models to predict the diagnosis based on blood cell data.
- **Pipeline Creation:** Develop pipelines for data ingestion, transformation, and model training.
- **Supporting Scripts:** Provide scripts for setup, logging, exception handling, and utility functions.

### 4. Project Structure  
```
├── artifacts/
│   ├── best_model.pkl
│   ├── LogisticRegression.pkl
│   ├── RidgeClassifier.pkl
│   ├── DecisionTreeClassifier.pkl
│   ├── RandomForestClassifier.pkl
│   ├── AdaBoostClassifier.pkl
│   ├── GradientBoostingClassifier.pkl
│   ├── XGBoostClassifier.pkl
│   ├── KNeighborsClassifier.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── data/
│   │   └── diagnosed_cbc_data_v4.csv
│   └── Diagnose_Anemia_Type.ipynb
│
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_training.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── med.jpeg
│   └── style.css
│
├── app.py
├── .gitignore
├── requirements.txt
├── README.md
└── setup.py
```

### 5. Data Ingestion  
The data ingestion module loads the blood cell analysis dataset, splits it into training and testing sets, and saves them for further use. The raw dataset is stored in the `artifacts/` folder.

### 6. Data Transformation  
The data transformation module preprocesses the dataset by encoding categorical variables (e.g., Diagnosis) and scaling numerical features (e.g., WBC, RBC, HGB). The transformed data is stored in the `artifacts/` folder.

### 7. Model Training  
The model training module trains several machine learning classification models, such as:

- Logistic Regression
- Ridge Classifier
- Decision Tree Classifier
- Random Forest Classifier
- AdaBoost Classifier
- Gradient Boosting Classifier
- KNeighbors Classifier
- XGB Classifier


![model_accuracy_comparison](https://github.com/user-attachments/assets/aba7cd6a-03c7-4d31-b9cb-98b378d2085b)


The best-performing model is saved as `best_model.pkl` in the `artifacts/` folder.

### 8. Training Pipeline  
The training pipeline integrates data ingestion, transformation, and model training, ensuring smooth execution from loading data to saving the trained model.

### 9. Prediction Pipeline  
The prediction pipeline uses `best_model.pkl` and `preprocessor.pkl` to predict the diagnosis based on new blood test data. It handles preprocessing and model inference seamlessly.

### 10. Flask (Web Interface)  
The Flask app provides a web interface where healthcare professionals can input patient blood test data and predict medical diagnoses. Input fields are handled by `index.html`, and results are displayed in `results.html`.


![Screenshot 10-09-2024 07 56 44](https://github.com/user-attachments/assets/782eb0d4-b793-47d0-8923-cb62d097ee69)

![Screenshot 10-09-2024 08 02 07](https://github.com/user-attachments/assets/93359428-4ba9-4021-b915-d3086b04bd46)


### 11. Logging  
The `logger.py` file captures logs for processes such as data ingestion, transformation, and model training, aiding in debugging and workflow monitoring.

### 12. Exception Handling  
The `exception.py` file ensures robust error handling by logging and addressing any issues encountered during project execution.

### 13. Utils  
The `utils.py` file includes utility functions for tasks such as directory creation, file management, and data loading.

### 14. Conclusion  
This documentation outlines the end-to-end workflow of the Blood Cell Analysis Prediction project, covering ingestion, transformation, modeling, and deployment. The project is designed to be modular and scalable, making it adaptable for future extensions.

