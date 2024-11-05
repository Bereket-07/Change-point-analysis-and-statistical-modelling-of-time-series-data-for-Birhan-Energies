// src/components/charts/HistoricalChart.js

import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function HistoricalChart({ data, predictions }) {
    // Merging historical data with predictions for visualization
    const chartData = data.map((item, index) => ({
        date: item.date,
        price: item.price,
        predicted_price: predictions[index]?.predicted_price || null
    }));

    return (
        <LineChart width={600} height={300} data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="price" stroke="#8884d8" name="Actual Price" />
            <Line type="monotone" dataKey="predicted_price" stroke="#82ca9d" name="Predicted Price" />
        </LineChart>
    );
}

export default HistoricalChart;
