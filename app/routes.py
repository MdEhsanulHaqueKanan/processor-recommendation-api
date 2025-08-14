# app/routes.py (The Final, Robust Version)

from flask import render_template, request, Blueprint, jsonify
from flask_cors import CORS
from app.services import (
    load_and_process_data,
    get_recommendations,
    load_ml_artifacts,
    predict_processor_function,
    predict_wireless_features
)
from config import Config
import pandas as pd
import numpy as np # Import numpy to handle NaN types

main = Blueprint('main', __name__)
CORS(main)

# --- GLOBAL DATA AND MODEL LOADING ---
df_processed = load_and_process_data(Config.DATA_FILE_PATH)
function_model, function_label_encoder, wireless_model = load_ml_artifacts(
    Config.FUNCTION_CLASSIFIER_PATH,
    Config.LABEL_ENCODER_PATH,
    Config.WIRELESS_PREDICTOR_PATH
)

# --- HELPER FUNCTION (Unchanged) ---
def _build_prediction_input_from_json(json_data):
    defaults = {
        'GPU Clock': 800, 'Total L2 Cache': 4096, 'Total L3 Cache': 8192,
        'bluetooth_version': 5.2, 'Semiconductor Technology': 'FinFET', 'Fab': 'TSMC',
        'has_wifi_6_or_higher': True, 'has_nfc': True, 'has_efficiency_cores': True
    }
    input_data = {
        'Designer': json_data.get('designer'),
        'Year Released': int(json_data.get('yearReleased', 0)),
        'Number of processor core(s)': int(json_data.get('numCores', 0)),
        'Feature Size': float(json_data.get('featureSize', 0.0)),
        'has_performance_cores': bool(json_data.get('hasPerformanceCores')),
        'has_5g': bool(json_data.get('has5g')),
    }
    return {**defaults, **input_data}

# --- API ROUTES ---

@main.route('/api/predict', methods=['POST'])
def api_predict():
    """Handles prediction requests from the React frontend."""
    if not (function_model and wireless_model): return jsonify({"error": "Models are not available."}), 500
    try:
        request_data = request.get_json()
        if not request_data: return jsonify({"error": "No input data provided."}), 400
        input_data_for_model = _build_prediction_input_from_json(request_data)
        function_prediction = predict_processor_function(function_model, function_label_encoder, input_data_for_model)
        wireless_prediction = predict_wireless_features(wireless_model, input_data_for_model)
        return jsonify({"primaryFunction": function_prediction, "wirelessCapabilities": wireless_prediction})
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({"error": f"Invalid input provided: {e}"}), 400
    except Exception as e:
        return jsonify({"error": "Could not make a prediction due to a server error."}), 500

@main.route('/api/recommend', methods=['POST'])
def api_recommend():
    """Handles recommendation requests from the React frontend."""
    try:
        requirements = request.get_json()
        if not requirements: return jsonify({"error": "No recommendation criteria provided."}), 400
        
        recommendations_df = get_recommendations(requirements, df_processed)
        
        # ====================================================================
        # --- THE FINAL BUG FIX IS HERE ---
        # ====================================================================

        # 1. Clean the data BEFORE mapping. Replace any missing 'serie' with a default.
        if 'serie' in recommendations_df.columns:
            recommendations_df['serie'] = recommendations_df['serie'].fillna('Unnamed Processor')
        
        # 2. Use the correct column names from your data.
        column_mapping = {
            'serie': 'name',
            'designer': 'designer',
            'year_released': 'releaseYear',
            'number_of_cores': 'cores'
        }
        
        existing_columns = [col for col in column_mapping.keys() if col in recommendations_df.columns]
        frontend_df = recommendations_df[existing_columns].rename(columns=column_mapping)
        
        # 3. Manually add boolean fields.
        frontend_df['has5g'] = True
        frontend_df['hasWifi6'] = True
        frontend_df['id'] = range(len(frontend_df))
        
        # 4. Convert to dictionary, which is now guaranteed to be safe for JSON.
        recommendations_list = frontend_df.to_dict('records')
        
        return jsonify(recommendations_list)
        
    except Exception as e:
        print(f"An unexpected error occurred during recommendation: {e}")
        return jsonify({"error": f"Could not fetch recommendations due to a server error: {e}"}), 500

# --- ORIGINAL WEB ROUTES (Now Obsolete) ---
@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/predict', methods=['GET'])
def predict():
    return render_template('predict.html')