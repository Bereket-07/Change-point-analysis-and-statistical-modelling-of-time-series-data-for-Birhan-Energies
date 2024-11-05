from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load your processed data
historical_data = pd.read_csv('../../data/combined_data.csv')
predictions = pd.read_csv('../../data/predictions.csv')
metrics = {
    "rmse": 0.305,
    "mae": 0.543,
    "r2": -27.25
}

# Define API endpoints
@app.route('/api/historical', methods=['GET'])
def get_historical_data():
    return jsonify(historical_data.to_dict(orient='records'))

@app.route('/api/predictions', methods=['GET'])
def get_predictions():
    return jsonify(predictions.to_dict(orient='records'))

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
