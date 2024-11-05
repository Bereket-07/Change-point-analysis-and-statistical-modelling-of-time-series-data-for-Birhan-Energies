// src/components/MetricsDisplay.js

import React from 'react';

function MetricsDisplay({ metrics }) {
    return (
        <div style={{ display: 'flex', gap: '20px', marginBottom: '20px' }}>
            <div className="metric-card">
                <h3>RMSE</h3>
                <p>{metrics.rmse}</p>
            </div>
            <div className="metric-card">
                <h3>MAE</h3>
                <p>{metrics.mae}</p>
            </div>
            <div className="metric-card">
                <h3>R²</h3>
                <p>{metrics.r2}</p>
            </div>
        </div>
    );
}

export default MetricsDisplay;
