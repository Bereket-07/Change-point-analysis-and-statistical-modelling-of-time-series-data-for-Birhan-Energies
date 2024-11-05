// src/components/Dashboard.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import HistoricalChart from './charts/HistoricalChart';
import MetricsDisplay from './MetricsDisplay';

function Dashboard() {
    const [historicalData, setHistoricalData] = useState([]);
    const [predictions, setPredictions] = useState([]);
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/historical')
            .then((response) => setHistoricalData(response.data))
            .catch(error => console.error('Error fetching historical data:', error));

        axios.get('http://127.0.0.1:5000/api/predictions')
            .then((response) => setPredictions(response.data))
            .catch(error => console.error('Error fetching predictions:', error));

        axios.get('http://127.0.0.1:5000/api/metrics')
            .then((response) => setMetrics(response.data))
            .catch(error => console.error('Error fetching metrics:', error));
    }, []);

    return (
        <div>
            <h1>Oil Price Dashboard</h1>
            <MetricsDisplay metrics={metrics} />
            <HistoricalChart data={historicalData} predictions={predictions} />
            {/* Add more charts and components as needed */}
        </div>
    );
}

export default Dashboard;
