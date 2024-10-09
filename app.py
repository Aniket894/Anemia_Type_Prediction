from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

class PredictionPipeline:
    def __init__(self, model_path, preprocessor_path):
        # Load the pre-trained model and preprocessor
        self.model = joblib.load(model_path)
        self.preprocessor = joblib.load(preprocessor_path)

    def predict(self, input_data):
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        # Transform the data using the preprocessor
        processed_data = self.preprocessor.transform(input_df)
        # Make predictions using the model
        predictions = self.model.predict(processed_data)
        return predictions.tolist()
    
# Initialize the prediction pipeline with model and preprocessor paths
prediction_pipeline = PredictionPipeline(
    model_path='artifacts/DecisionTreeClassifier.pkl',
    preprocessor_path='artifacts/preprocessor.pkl'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    input_data = {
        'WBC': float(request.form.get('WBC')),
        'LYMp': float(request.form.get('LYMp')),
        'NEUTp': float(request.form.get('NEUTp')),
        'LYMn': float(request.form.get('LYMn')),
        'NEUTn': float(request.form.get('NEUTn')),
        'RBC': float(request.form.get('RBC')),
        'HGB': float(request.form.get('HGB')),
        'HCT': float(request.form.get('HCT')),
        'MCV': float(request.form.get('MCV')),
        'MCH': float(request.form.get('MCH')),
        'MCHC': float(request.form.get('MCHC')),
        'PLT': float(request.form.get('PLT')),
        'PDW': float(request.form.get('PDW')),
        'PCT': float(request.form.get('PCT'))
    }

    # Make prediction
    predictions = prediction_pipeline.predict(input_data)
    
    return render_template('results.html', predictions=predictions)
    
if __name__ == '__main__':
    app.run(debug=True)
