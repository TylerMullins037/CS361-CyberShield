# Project Overview
This project aims to develop a real-time threat intelligence system and a risk
management framework for ShopSmart Solutions, an e-commerce platform. Each
group of five students will collaborate to analyze threats, vulnerabilities, and assets
(TVA), conduct risk assessments, and implement risk treatment strategies. The project
will incorporate Open Source Intelligence (OSINT) tools, automation via Large Language
Models (LLMs), and alignment with the NIST Risk Management Framework (RMF) and
NIST Cybersecurity Framework (CSF) 2.0.


-----------------------------------------------------------------------------------------


🗓️ Week 6 Real-Time Risk Alerts, Incident Response, and Cost-Benefit Analysis for Risk Treatment (26 – 30 March 2025)
Focus:
Implementing real-time risk alerts, building incident response workflows, integrating cost-benefit analysis for risk treatment, enhancing the threat intelligence dashboard with risk trends, and optimizing system performance.

🔍 Overview
In Week 6, the team focused on implementing a robust alerting system for high-risk threats, automating incident response procedures, and integrating cost-benefit analysis (CBA) for security decision-making. The threat intelligence dashboard was enhanced with real-time risk insights and trends, and API performance was optimized to improve system efficiency.

✅ Tasks Completed
🚨 1. Real-Time Risk Alerts for Detected Threats
Developed a real-time notification system to alert stakeholders when threats exceed a Risk Score > 20.

Implemented email and webhook alerts for critical cybersecurity events.

Stored alert logs in the database for historical tracking and analysis.

🛡️ 2. Incident Response Mechanism
Built an incident response workflow that automatically suggests countermeasures based on detected threats.

Linked response plans to NIST's Incident Handling Guide (SP 800-61 Rev. 2).

Integrated incident logs into the database for tracking and analysis.

💰 3. Cost-Benefit Analysis (CBA) for Risk Treatment
Implemented an automated CBA calculation script to compare the financial impact of security controls.

Integrated Annual Loss Expectancy (ALE) before and after mitigation to support informed decision-making.

CBA results now provide a clear view of the value of implemented security measures.

📊 4. Enhanced Threat Intelligence Dashboard
Added new dashboard components to display real-time risk trends, security insights, and mitigation outcomes.

Implemented filtering options to view threats by severity, type, and impact.

Visualizations now offer a clearer view of evolving threat landscapes.

⚡ 5. Optimizing API Calls and Threat Data Storage
Improved API request efficiency by reducing redundant calls.

Integrated caching mechanisms (e.g., Redis) to temporarily store threat intelligence results for faster access.

Optimized threat data storage to enhance system performance and scalability.

📂 Files Added/Updated
File/Directory	Description
/src/alerts.py	Real-time alert system for high-risk threats
/db/alerts.sql	Database schema for alert logs
/src/incident_response.py	Incident response mechanism with countermeasures
/db/incident_logs.sql	Incident handling logs schema
/src/cba_analysis.py	CBA automation script for risk treatment
/src/components/Dashboard.js	Enhanced threat intelligence dashboard UI
/src/api_optimizer.py	API optimization and caching improvements
📌 All Deliverables Submitted by: 30 March 2025


-----------------------------------------------------------------------------------------


🗓️ Week 5 Risk Analysis, Automated Risk Scoring, and Threat Mitigation Planning (19 – 23 March 2025)
Focus:
Enhancing risk scoring using machine learning (LLM), refining TVA mapping, developing dynamic risk prioritization models, and automating risk mitigation recommendations.

🔍 Overview
In Week 5, the team advanced the platform by incorporating machine learning models for dynamic risk analysis, refining the threat-vulnerability-asset (TVA) mapping using live OSINT intelligence, and creating a system for automated risk mitigation. Additionally, a dynamic risk prioritization model was developed to assess and highlight critical threats, and blue team capabilities were enhanced by linking mitigation strategies to real-time alerts.

✅ Tasks Completed
🤖 1. LLM-Based Risk Scoring
Integrated GPT-4 or Hugging Face models to dynamically analyze threat data and adjust risk scores.

Developed a script for real-time AI-powered risk assessments.

🔄 2. Refining TVA Mapping Using OSINT Intelligence
Updated TVA mappings based on live threat intelligence.

Adjusted likelihood and impact values for threats like phishing, SQL injection, and DDoS based on real-time data.

📊 3. Dynamic Risk Prioritization Model
Developed an algorithm to prioritize threats dynamically based on their risk scores.

Implemented a weighted scoring system to highlight high-priority risks for immediate attention.

⚙️ 4. Automated Risk Mitigation Recommendations
Created an automated system to generate mitigation strategies for various detected threats.

Integrated mitigation strategies into the dashboard for real-time blue team actions.

🛡️ 5. Blue Teaming & Incident Response Integration
Integrated blue team capabilities by linking risk mitigation recommendations to threat alerts.

Developed response playbooks for each detected threat to guide incident management.

📂 Files Added/Updated
File/Directory	Description
/src/risk_analysis.py	LLM-based risk scoring script
/db/tva_update.sql	Updated TVA mapping script
/src/risk_prioritization.py	Dynamic risk prioritization model
/src/mitigation_recommendations.py	Automated risk mitigation recommendations
/src/incident_response.py	Blue team response module and incident playbooks


-----------------------------------------------------------------------------------------


# 🗓️ Week 4 Real-Time Threat Intelligence Integration (12 – 16 March 2025)

**Focus:**  
Integrating real-time threat intelligence through OSINT APIs, automated updates, alerting systems, and live data visualization.

---

## 🔍 Overview  
In Week 4, the team advanced the platform by implementing real-time threat intelligence features. This included integrating external OSINT APIs, automating data updates, building a real-time dashboard, and implementing alert mechanisms for high-risk threats. Comprehensive testing was also carried out to validate all threat data pipelines.

---

## ✅ Tasks Completed

### 🌐 1. OSINT API Integration
- Integrated APIs from:
  - **Shodan**
  - **Have I Been Pwned**
  - **VirusTotal**
- Backend scripts fetch and store threat data in PostgreSQL.
- API endpoints implemented in `/api/`.

---

### 🔄 2. Automated Threat Intelligence Updates
- Developed a scheduler to fetch new threat data every 6 hours.
- Enabled historical logging of OSINT data for trend analysis.
- Auto-update script added to `/api/scheduler.py`.

---

### 📊 3. Real-Time Threat Dashboard
- Built a React component to display incoming threat intelligence.
- Features:
  - Dynamic threat logs
  - Risk scores
  - Filter and sort functionality
- Dashboard UI component committed to `/src/components/ThreatDashboard.js`.

---

### 🚨 4. High-Risk Alert System
- Implemented alerting for threats with Risk Score > 20.
- Alerts sent via email or webhook to system administrators.
- Alert logic implemented in `/src/alerts.py`.

---

### ✅ 5. API Testing and Validation
- Conducted unit tests to ensure OSINT API integrations fetch accurate data.
- Test scripts implemented in `/tests/api_tests.py`.

---

## 📂 Files Added/Updated

| File/Directory                         | Description                                |
|----------------------------------------|--------------------------------------------|
| `/api/shodan_integration.py`          | Shodan API integration script              |
| `/api/scheduler.py`                   | Auto-update scheduler for threat data      |
| `/src/components/ThreatDashboard.js`  | Real-time dashboard UI component           |
| `/src/alerts.py`                      | Alert system for high-risk threats         |
| `/tests/api_tests.py`                 | Unit tests for API validation              |

---

## 📌 All Deliverables Submitted by: **16 March 2025**

-----------------------------------------------------------------------------------------

# 🗓️ Week 3 Asset Identification & Threat-Vulnerability-Asset (TVA) Mapping (5 – 9 March 2025)

**Focus:**  
Asset cataloging, TVA (Threat-Vulnerability-Asset) mapping, OSINT data ingestion, and backend/frontend setup for risk assessment visualization.

---

## 🔍 Overview  
In Week 3, the team focused on identifying ShopSmart Solutions’ critical assets, mapping them to relevant threats and vulnerabilities, and integrating external OSINT feeds to support dynamic risk assessments. Foundational components were also developed to power the real-time risk dashboard.

---

## ✅ Tasks Completed

### 🗂️ 1. Asset Inventory Creation
- Cataloged 5 asset categories:
  - Hardware
  - Software
  - Data
  - Personnel
  - Business Processes
- Structured entries for database integration and tagging.

---

### 🔗 2. TVA Mapping Structure
- Designed a relational schema to connect:
  - Assets → Threats → Vulnerabilities
- Included logic for:
  - Likelihood scoring
  - Impact ratings
  - Initial risk score generation

---

### 🌐 3. OSINT Data Integration
- Ingested live data using external APIs.
- Parsed and normalized threat data to align with internal TVA schema.
- Scripts uploaded to `/api/osint_ingestion.py`.

---

### ⚙️ 4. Risk Assessment Logic
- Implemented rule-based scoring engine using Deepseek LLM.
- Back-end module generates real-time risk scores per asset.
- Positioned for later enhancement with ML-based scoring.

---

### 📊 5. Threat Intelligence Dashboard
- Created frontend components to:
  - Display mapped assets and their associated risks.
  - Show real-time updates from OSINT feeds.
- Component added to `/src/components/TVAMapDashboard.js`.

---

## 📂 Files Added/Updated

| File/Directory                           | Description                                      |
|------------------------------------------|--------------------------------------------------|
| `/db/assets_table.sql`                  | Structured asset categories and sample entries   |
| `/db/tva_mapping.sql`                   | TVA mapping schema and example data              |
| `/api/osint_ingestion.py`               | Script to ingest and normalize OSINT data        |
| `/src/logic/risk_engine.py`             | Rule-based risk assessment using Deepseek LLM    |
| `/src/components/TVAMapDashboard.js`    | Frontend dashboard for asset-risk visualization  |

---

## 📌 All Deliverables Submitted by: **9 March 2025**

-----------------------------------------------------------------------------------------


# 🗓️ Week 2 Setting Up the Web Application & OSINT API Research (26 February – 2 March 2025)

**Focus:**  
Setting up the web application framework and conducting OSINT API research.

---

## 🔍 Overview  
In Week 2, the team focused on laying the foundational architecture for the Threat Intelligence Platform. This included backend and frontend setup, database schema design, integration of open-source intelligence (OSINT) APIs, and developing a prototype dashboard layout.

---

## ✅ Tasks Completed

### 🔧 1. Web Application Framework Setup
- **Backend:**
  - Initialized Flask application with basic route handling in `app.py`.
- **Frontend:**
  - Created initial React project with routing and a login screen.
- **Commits:**
  - Web app structure committed to Git under `/src/`.

---

### 🗃️ 2. Database Schema Design
- Created schema for:
  - `assets`
  - `threats`
  - `vulnerabilities`
  - `risk_ratings`
- Uploaded schema file to `/db/schema.sql`.

---

### 🌐 3. OSINT API Research & Integration
- Researched and selected three OSINT APIs:
  - **Shodan** 
  - **Security Trails** 
  - **Virus Total** 
- Created test scripts for API integration.
- Added usage documentation to `/docs/api_research.md`.
- Uploaded working scripts to `/api/`.

---

### 📊 4. Dashboard UI Development
- Developed initial React component for the dashboard.
- Created placeholder UI for:
  - Threat Logs
  - Risk Scores
  - Live Alerts
- Component committed to `/src/components/ThreatDashboard.js`.

---

## 📂 Files Added/Updated

| File/Directory                   | Description                          |
|----------------------------------|--------------------------------------|
| `/src/`                          | React app and Flask backend setup    |
| `/db/schema.sql`                | Initial PostgreSQL database schema   |
| `/api/`                          | OSINT API integration scripts        |
| `/docs/api_research.md`         | API documentation and research notes |
| `/src/components/ThreatDashboard.js` | Initial dashboard UI component    |

---

## 📌 All Deliverables Submitted by: **2 March 2025**

