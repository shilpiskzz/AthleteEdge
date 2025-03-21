from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("injury_recovery_model.pkl")

# Expected categorical mappings (Ensure this matches how your model was trained)
injury_types = ['Toe Injury', 'Ankle Injury', 'Finger Injury', 'Hamstring Niggle', 'Knee Niggle', 'Shoulder Injury']
genders = ['M', 'F']
injury_severity = ['major', 'minor']

# Define input schema
class InjuryData(BaseModel):
    Callorie: int
    Age: int
    Weight: int
    Fitness_Level: float
    Injury: str  # Categorical
    Gender: str  # Categorical
    Type: str  # Categorical

@app.post("/predict-recovery")
def predict_recovery(data: InjuryData):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # One-Hot Encode categorical variables
        for col, categories in zip(['Injury', 'Gender', 'Type'], [injury_types, genders, injury_severity]):
            for category in categories:
                input_df[f"{col}_{category}"] = 1 if input_df[col].iloc[0] == category else 0
        
        # Drop original categorical columns
        input_df = input_df.drop(columns=['Injury', 'Gender', 'Type'])

        # Ensure input columns match model's expected columns
        model_features = model.feature_names_in_
        input_df = input_df.reindex(columns=model_features, fill_value=0)

        # Predict recovery period
        prediction = model.predict(input_df)[0]

        return {"Predicted_Recovery_Period": round(prediction, 2)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run API using: uvicorn api:app --host 0.0.0.0 --port 8000
