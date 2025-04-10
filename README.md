# Project Overview
This project aims to develop a real-time threat intelligence system and a risk
management framework for ShopSmart Solutions, an e-commerce platform. Each
group of five students will collaborate to analyze threats, vulnerabilities, and assets
(TVA), conduct risk assessments, and implement risk treatment strategies. The project
will incorporate Open Source Intelligence (OSINT) tools, automation via Large Language
Models (LLMs), and alignment with the NIST Risk Management Framework (RMF) and
NIST Cybersecurity Framework (CSF) 2.0.

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

