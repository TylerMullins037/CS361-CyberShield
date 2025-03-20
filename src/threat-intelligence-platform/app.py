from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_cors import CORS
import psycopg2
import os
import logging

app = Flask(__name__, static_folder="threat-dashboard/build", static_url_path="")
CORS(app)  # Allow frontend to access API


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="defaultdb", 
            user="doadmin", 
            password="***************",
            port = "25060", 
            host="******************",
            sslmode="require"  # Ensures secure connection
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None



# Serve React frontend
@app.route('/')
def serve_react_app():
    return send_from_directory(app.static_folder, "index.html")

# Fetch assets from database
@app.route('/api/assets', methods=['GET'])
def get_assets():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT id, asset_name, asset_type, description FROM assets")
    assets = [
        {"id": row[0], "asset_name": row[1], "asset_type": row[2], "description": row[3]}
        for row in cursor.fetchall()
    ]
    cursor.close()
    conn.close()
    return jsonify(assets)

# Fetch threats from database
@app.route('/api/threats', methods=['GET'])
def get_threats():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT threat_name, vulnerability_description, likelihood, impact, likelihood * impact AS risk_score FROM tva_mapping")
    threats = [
        {"name": row[0], "vulnerability": row[1], "likelihood": row[2], "impact": row[3], "risk_score": row[4]}
        for row in cursor.fetchall()
    ]
    cursor.close()
    conn.close()
    return jsonify(threats)

@app.route('/api/threat_data', methods=['GET'])
def get_threats_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    cursor = conn.cursor()
    cursor.execute("SELECT ip_address, ports, services FROM threat_data")
    threats_data = [
        {"ip_address": row[0], "ports": row[1], "services": row[2]}
        for row in cursor.fetchall()
    ]
    
    cursor.close()
    conn.close()
    return jsonify(threats_data)

# Fetch high-risk threats by parsing the API response
@app.route('/api/high_risk_threats', methods=['GET'])
def get_high_risk_threats():
    try:
        # Internal API call to fetch all threats
        response = requests.get("http://127.0.0.1:5000/api/threats")
        
        if response.status_code != 200:
            return jsonify({"error": "Failed to retrieve threats from API"}), 500

        threats = response.json()

        # Filter threats with risk score > 20
        high_risk_threats = [threat for threat in threats if threat["risk_score"] > 19]

        return jsonify(high_risk_threats)

    except Exception as e:
        return jsonify({"error": f"Internal processing error: {str(e)}"}), 500

# Serve static files (JS, CSS, images, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
