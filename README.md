# Project Overview
This project aims to develop a real-time threat intelligence system and a risk
management framework for ShopSmart Solutions, an e-commerce platform. Each
group of five students will collaborate to analyze threats, vulnerabilities, and assets
(TVA), conduct risk assessments, and implement risk treatment strategies. The project
will incorporate Open Source Intelligence (OSINT) tools, automation via Large Language
Models (LLMs), and alignment with the NIST Risk Management Framework (RMF) and
NIST Cybersecurity Framework (CSF) 2.0.


-----------------------------------------------------------------------------------------


# 🗓️ Week 7 Fine-Tuning Risk Scoring, Threat Report Generation, and Security Audits (10 April 2025)

## Focus:
Refining the risk scoring model, developing comprehensive threat report generation features, conducting initial security audits, and optimizing data logging and database performance.

---

## 🔍 Overview
In Week 7, the team focused on fine-tuning the risk scoring system by incorporating real-time threat intelligence, automating threat report generation, and conducting initial security audits to identify vulnerabilities. Data logging for threat events was optimized for better forensic tracking, and database performance was enhanced to handle large datasets effectively.

---

## ✅ Tasks Completed

### 📊 1. Fine-Tuning Risk Scoring Based on Threat Intelligence Trends
- Updated the risk scoring model to reflect real-time threat intelligence trends.
- Incorporated machine learning-based trend analysis for forecasting future risks.
- Implemented time-weighted risk scoring to prioritize current, active threats.

### 📑 2. Developing a Comprehensive Threat Report Generation Feature
- Automated the generation of PDF/CSV reports summarizing risk assessments and incidents.
- Included detailed threat intelligence summaries, risk scores, and mitigation plans for each report.

### 🛠️ 3. Conducting Initial Security Audits
- Performed penetration testing using OWASP ZAP, Nmap, and Burp Suite.
- Identified vulnerabilities, misconfigurations, and security weaknesses within the system.
- Documented findings and provided recommendations for mitigation.

### 📝 4. Optimizing Data Logging & Threat Event Tracking
- Implemented structured logging for detailed tracking of each security event.
- Improved logging performance with log rotation to prevent bottlenecks during high activity.

### ⚙️ 5. Ensuring Database Integrity & Performance Optimization
- Optimized SQL queries and added indexing to improve query performance.
- Developed and tested backup and restore procedures to ensure database integrity.

---

## 📂 Files Added/Updated

| File/Directory                         | Description                                    |
|----------------------------------------|------------------------------------------------|
| `/src/threat-intelligence-platform/risk_scoring.py`                 | Updated risk scoring model with real-time intelligence |
| `/src/threat-intelligence-platform/report_generator.py`             | Automated threat report generation system     |
| `/docs/security_audit.md`              | Security audit report with findings and recommendations |
| `/src/threat-intelligence-platform/logging.py`                      | Threat event logging system                    |
| `/db/optimized_queries.sql`            | Optimized SQL queries for performance         |

---

📌 All Deliverables Submitted: **8 April 2025**



-----------------------------------------------------------------------------------------


# 🗓️ Week 6 Real-Time Risk Alerts, Incident Response, and Cost-Benefit Analysis for Risk Treatment (5 April 2025)

## Focus:
Implementing real-time risk alerts, building incident response workflows, integrating cost-benefit analysis for risk treatment, enhancing the threat intelligence dashboard with risk trends, and optimizing system performance.

---

## 🔍 Overview
In Week 6, the team focused on implementing a robust alerting system for high-risk threats, automating incident response procedures, and integrating cost-benefit analysis (CBA) for security decision-making. The threat intelligence dashboard was enhanced with real-time risk insights and trends, and API performance was optimized to improve system efficiency.

---

## ✅ Tasks Completed

### 🚨 1. Real-Time Risk Alerts for Detected Threats
- Developed a real-time notification system to alert stakeholders when threats exceed a Risk Score > 20.
- Implemented email and webhook alerts for critical cybersecurity events.
- Stored alert logs in the database for historical tracking and analysis.

### 🛡️ 2. Incident Response Mechanism
- Built an incident response workflow that automatically suggests countermeasures based on detected threats.
- Linked response plans to NIST's Incident Handling Guide (SP 800-61 Rev. 2).
- Integrated incident logs into the database for tracking and analysis.

### 💰 3. Cost-Benefit Analysis (CBA) for Risk Treatment
- Implemented an automated CBA calculation script to compare the financial impact of security controls.
- Integrated Annual Loss Expectancy (ALE) before and after mitigation to support informed decision-making.
- CBA results now provide a clear view of the value of implemented security measures.

### 📊 4. Enhanced Threat Intelligence Dashboard
- Added new dashboard components to display real-time risk trends, security insights, and mitigation outcomes.
- Implemented filtering options to view threats by severity, type, and impact.
- Visualizations now offer a clearer view of evolving threat landscapes.

### ⚡ 5. Optimizing API Calls and Threat Data Storage
- Improved API request efficiency by reducing redundant calls.
- Integrated caching mechanisms (e.g., Redis) to temporarily store threat intelligence results for faster access.
- Optimized threat data storage to enhance system performance and scalability.

---

## 📂 Files Added/Updated

| File/Directory                         | Description                                    |
|----------------------------------------|------------------------------------------------|
| `/src/threat-intelligence-platform/alerts.py`                       | Real-time alert system for high-risk threats   |
| `/db/alert_logs.sql`                       | Database schema for alert logs                 |
| `/src/threat-intelligence-platform/incident_response.py`            | Incident response mechanism with countermeasures|
| `/db/incident_logs.sql`                | Incident handling logs schema                  |
| `/src/threat-intelligence-platform/cba_analysis.py`                 | CBA automation script for risk treatment       |
| `/src/threat-dashboard/src/components/Dashboard.js`        | Enhanced threat intelligence dashboard UI      |
| `/api/api_optimizer.py`                | API optimization and caching improvements      |

---

📌 All Deliverables Submitted: **2 April 2025**


-----------------------------------------------------------------------------------------


# 🗓️ Week 5 Risk Analysis, Automated Risk Scoring, and Threat Mitigation Planning (1 April 2025)

## Focus:
Enhancing risk scoring using machine learning (LLM), refining TVA mapping, developing dynamic risk prioritization models, and automating risk mitigation recommendations.

---

## 🔍 Overview
In Week 5, the team advanced the platform by incorporating machine learning models for dynamic risk analysis, refining the threat-vulnerability-asset (TVA) mapping using live OSINT intelligence, and creating a system for automated risk mitigation. Additionally, a dynamic risk prioritization model was developed to assess and highlight critical threats, and blue team capabilities were enhanced by linking mitigation strategies to real-time alerts.

---

## ✅ Tasks Completed

### 🤖 1. LLM-Based Risk Scoring
- Integrated GPT-4 or Hugging Face models to dynamically analyze threat data and adjust risk scores.
- Developed a script for real-time AI-powered risk assessments.

### 🔄 2. Refining TVA Mapping Using OSINT Intelligence
- Updated TVA mappings based on live threat intelligence.
- Adjusted likelihood and impact values for threats like phishing, SQL injection, and DDoS based on real-time data.

### 📊 3. Dynamic Risk Prioritization Model
- Developed an algorithm to prioritize threats dynamically based on their risk scores.
- Implemented a weighted scoring system to highlight high-priority risks for immediate attention.

### ⚙️ 4. Automated Risk Mitigation Recommendations
- Created an automated system to generate mitigation strategies for various detected threats.
- Integrated mitigation strategies into the dashboard for real-time blue team actions.

### 🛡️ 5. Blue Teaming & Incident Response Integration
- Integrated blue team capabilities by linking risk mitigation recommendations to threat alerts.
- Developed response playbooks for each detected threat to guide incident management.

---

## 📂 Files Added/Updated

| File/Directory                        | Description                                             |
|---------------------------------------|---------------------------------------------------------|
| `/src/threat-intelligence-platform/risk_analysis.py`               | LLM-based risk scoring script                           |
| `/db/tva_update.sql`                  | Updated TVA mapping script                              |
| `/src/threat-intelligence-platform/risk_prioritization.py`         | Dynamic risk prioritization model                       |
| `/src/threat-intelligence-platform/mitigation_recommendations.py`  | Automated risk mitigation recommendations               |
| `/src/threat-intelligence-platform/incident_response.py`          | Blue team response module and incident playbooks        |

## 📌 All Deliverables Submitted: **24 March 2025**


-----------------------------------------------------------------------------------------


# 🗓️ Week 4 Real-Time Threat Intelligence Integration (21 March 2025)

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
  - **SecurityTrails**
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
- Alert logic implemented in `/src/threat-intelligence-platform/alerts.py`.

---

### ✅ 5. API Testing and Validation
- Conducted unit tests to ensure OSINT API integrations fetch accurate data.
- Test scripts implemented in `/api/tests/api_tests.py`.

---

## 📂 Files Added/Updated

| File/Directory                         | Description                                |
|----------------------------------------|--------------------------------------------|
| `/api/shodan_integration.py`          | Shodan API integration script              |
| `/api/scheduler.py`                   | Auto-update scheduler for threat data      |
| `/src/threat-dashboard/src/components/ThreatDashboard.js`  | Real-time dashboard UI component           |
| `/src/threat-intelligence-platform/alerts.py`                      | Alert system for high-risk threats         |
| `/api/tests/api_tests.py`                 | Unit tests for API validation              |

---

## 📌 All Deliverables Submitted: **20 March 2025**

-----------------------------------------------------------------------------------------

# 🗓️ Week 3 Asset Identification & Threat-Vulnerability-Asset (TVA) Mapping (16 March 2025)

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
- Component added to `/src/threat-dashboard/src/components/Dashboard.js`.

---

## 📂 Files Added/Updated

| File/Directory                           | Description                                      |
|------------------------------------------|--------------------------------------------------|
| `/db/assets.sql`                  | Structured asset categories and sample entries   |
| `/db/tva_mapping.sql`                   | TVA mapping schema and example data              |
| `/api/osint_ingestion.py`               | Script to ingest and normalize OSINT data        |
| `/src/threat-intelligence-platform//risk_analysis.py`             | Rule-based risk assessment using Deepseek LLM    |
| `/src/threat-dashboard/src/components/Dashboard.js`    | Frontend dashboard for asset-risk visualization  |

---

## 📌 All Deliverables Submitted: **9 March 2025**

-----------------------------------------------------------------------------------------


# 🗓️ Week 2 Setting Up the Web Application & OSINT API Research (5 March 2025)

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
- Component committed to `/src/threat-dasboard/src/components/Dashboard.js`.

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

## 📌 All Deliverables Submitted: **28 Feb 2025**

