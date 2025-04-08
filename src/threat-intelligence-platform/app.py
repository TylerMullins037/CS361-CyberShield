from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_cors import CORS
import psycopg2
from fpdf import FPDF
import csv
import os
from datetime import datetime
from report_generator import ThreatReport


app = Flask(__name__, static_folder="threat-dashboard/build", static_url_path="")
CORS(app)  # Allow frontend to access API


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="defaultdb", 
            user="doadmin", 
            password="******",
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
  
@app.route('/api/risk-trends', methods=['GET'])
def get_risk_trends():
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = conn.cursor()

        # Query to join 'tva_mapping' and 'mitigation_strategies' tables to get threats and their associated strategies
        cursor.execute("""
                              SELECT 
        DATE(alert_date) as date,
        COUNT(*) as count
      FROM 
        alert_logs
      GROUP BY 
        DATE(alert_date)
      ORDER BY 
        date ASC;
    ;
        """)
        
        # Fetch the data from the query and format it into a list of dictionaries
        risk_trends = [
            {"date": row[0], "count": row[1]}
            for row in cursor.fetchall()
        ]
        
        cursor.close()
        conn.close()
        
        return jsonify(risk_trends)
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



# Add new routes to your Flask app:

@app.route('/api/generate-pdf-report', methods=['GET'])
def generate_pdf_report():
    try:
        # Get data from database
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = conn.cursor()
        
        # Get threats
        cursor.execute("SELECT threat_name, vulnerability_description, likelihood, impact, likelihood * impact AS risk_score, date FROM tva_mapping")
        threats = [
            {"name": row[0], "vulnerability": row[1], "likelihood": row[2], "impact": row[3], "risk_score": row[4], "date": row[5]}
            for row in cursor.fetchall()
        ]
        
        # Get mitigation strategies
        cursor.execute("""
            SELECT 
                t.threat_name,
                ms.mitigation_strategy AS mitigation_strategy
            FROM 
                mitigation_strategies ms
            JOIN 
                tva_mapping t ON ms.tva_mapping_id = t.id
        """)
        
        mitigations = [
            {"threat": row[0], "strategies": row[1]}
            for row in cursor.fetchall()
        ]
        
        # Create directory for reports if it doesn't exist
        os.makedirs("reports", exist_ok=True)
        
        # Generate PDF
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"reports/threat_report_{timestamp}.pdf"
        
        pdf = ThreatReport()
        pdf.add_page()
        
        # Add timestamp
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(10)
        
        # Add threats section
        pdf.add_section_title("Threat Assessment")
        for threat in threats:
            pdf.add_threat(
                threat["name"], 
                threat["risk_score"], 
                threat["vulnerability"],
                threat["likelihood"],
                threat["impact"],
                str(threat["date"]) if threat["date"] else None
            )
            
        # Add new page for mitigation strategies
        pdf.add_page()
        pdf.add_section_title("Mitigation Strategies")
        
        for mitigation in mitigations:
            pdf.add_mitigation(mitigation["threat"], mitigation["strategies"])
        
        pdf.output(pdf_filename)
        
        cursor.close()
        conn.close()
        
        return jsonify({"success": True, "file": pdf_filename})
    
    except Exception as e:
        return jsonify({"error": f"Failed to generate PDF report: {str(e)}"}), 500

@app.route('/api/generate-csv-report', methods=['GET'])
def generate_csv_report():
    try:
        # Get data from database
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = conn.cursor()
        
        # Get threats
        cursor.execute("SELECT threat_name, vulnerability_description, likelihood, impact, likelihood * impact AS risk_score, date FROM tva_mapping")
        threats = [
            {"name": row[0], "vulnerability": row[1], "likelihood": row[2], "impact": row[3], "risk_score": row[4], "date": row[5]}
            for row in cursor.fetchall()
        ]
        
        # Create directory for reports if it doesn't exist
        os.makedirs("reports", exist_ok=True)
        
        # Generate CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"reports/threat_report_{timestamp}.csv"
        
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['Threat', 'Vulnerability', 'Likelihood', 'Impact', 'Risk Score', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for threat in threats:
                writer.writerow({
                    'Threat': threat["name"],
                    'Vulnerability': threat["vulnerability"],
                    'Likelihood': threat["likelihood"],
                    'Impact': threat["impact"],
                    'Risk Score': threat["risk_score"],
                    'Date': threat["date"]
                })
        
        cursor.close()
        conn.close()
        
        return jsonify({"success": True, "file": csv_filename})
    
    except Exception as e:
        return jsonify({"error": f"Failed to generate CSV report: {str(e)}"}), 500

# Add a route to download generated reports
@app.route('/reports/<path:filename>', methods=['GET'])
def download_report(filename):
    return send_from_directory('reports', filename)

# Serve static files (JS, CSS, images, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
