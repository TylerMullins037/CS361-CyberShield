from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_cors import CORS
import psycopg2


app = Flask(__name__, static_folder="threat-dashboard/build", static_url_path="")
CORS(app)  # Allow frontend to access API


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="defaultdb", 
            user="doadmin", 
            password="",
            port = "25060", 
            host="db-postgresql-nyc3-21525-do-user-20065838-0.k.db.ondigitalocean.com",
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
    cursor.execute("SELECT threat_name, vulnerability_description, likelihood, impact, likelihood * impact AS risk_score, date FROM tva_mapping")
    threats = [
        {"name": row[0], "vulnerability": row[1], "likelihood": row[2], "impact": row[3], "risk_score": row[4], "date": row[5]}
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
    cursor.execute("SELECT ip_address, ports, services, threat_type FROM threat_data")
    threats_data = [
        {"ip_address": row[0], "ports": row[1], "services": row[2], "Threat": row[3]}
        for row in cursor.fetchall()
    ]
    
    cursor.close()
    conn.close()
    return jsonify(threats_data)

# Fetch high-risk threats by parsing the API response
@app.route('/api/high_risk_threats', methods=['GET'])
def get_high_risk_threats():
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = conn.cursor()

        # Query to join 'tva_mapping' and 'mitigation_strategies' tables to get threats and their associated strategies
        cursor.execute("""
                        SELECT 
                            t.threat_name,
                            t.risk_score,
                            ms.mitigation_strategy AS mitigation_strategy,
                            ms.tva_mapping_id
                        FROM 
                            tva_mapping t
                        JOIN 
                            mitigation_strategies ms ON ms.tva_mapping_id = t.id
                        WHERE
                            t.risk_score > 10;
        """)
        
        # Fetch the data from the query and format it into a list of dictionaries
        mitigation_data = [
            {"threat": row[0], "risk_score": row[1], "strategies": row[2], "id": row[3]}
            for row in cursor.fetchall()
        ]
        
        cursor.close()
        conn.close()
        
        return jsonify(mitigation_data)
    except Exception as e:
        return jsonify({"error": f"Internal processing error: {str(e)}"}), 500
  
    
    
@app.route('/api/mitigation-strategies', methods=['GET'])
def get_mitigation_strategies():
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = conn.cursor()

        # Query to join 'tva_mapping' and 'mitigation_strategies' tables to get threats and their associated strategies
        cursor.execute("""
                        SELECT 
                            t.threat_name,
                            ms.mitigation_strategy AS mitigation_strategy
                        FROM 
                            mitigation_strategies ms
                        JOIN 
                            tva_mapping t ON ms.tva_mapping_id = t.id;
        """)
        
        # Fetch the data from the query and format it into a list of dictionaries
        mitigation_data = [
            {"threat": row[0], "strategies": row[1]}
            for row in cursor.fetchall()
        ]
        
        cursor.close()
        conn.close()
        
        return jsonify(mitigation_data)
    except Exception as e:
        return jsonify({"error": f"Internal processing error: {str(e)}"}), 500
  
@app.route('/webhook-handler', methods=['POST'])
def handle_webhook():
    data = request.json
    print(f"Received Webhook: {data}")  # Log the data for debugging

    # Process the data (e.g., alert admin, update database, etc.)
    
    return jsonify({"status": "success"}), 200  # Respond to sender


# Serve static files (JS, CSS, images, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
