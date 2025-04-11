# ShopSmart Solutions Threat Intelligence Dashboard

## User Guide for Blue Team Analysts  
**Version 1.0**  
**Last Updated: April 11, 2025**

---

## Table of Contents

- [Introduction](#introduction)  
- [Getting Started](#getting-started)  
- [Dashboard Overview](#dashboard-overview)  
- [Monitoring Assets](#monitoring-assets)  
- [Analyzing Threats](#analyzing-threats)  
- [Advanced Threat Filtering](#advanced-threat-filtering)  
- [Understanding Risk Scores](#understanding-risk-scores)  
- [Reviewing Mitigation Strategies](#reviewing-mitigation-strategies)  
- [Generating Reports](#generating-reports)  
- [Best Practices](#best-practices)  
- [Quick Reference](#quick-reference)  

---

## Introduction

Welcome to the **ShopSmart Solutions Threat Intelligence Dashboard** – your central command center for monitoring, analyzing, and responding to security threats across your organization's digital infrastructure.

This user guide is specifically designed for blue team analysts and provides practical instructions on using the dashboard effectively to enhance your organization's security posture.

### Purpose of the Dashboard

The dashboard serves as a real-time threat intelligence platform that helps you:

- Monitor all digital assets in your environment  
- Identify and prioritize security threats  
- Understand risk levels and trends  
- Implement effective mitigation strategies  
- Generate comprehensive security reports  

---

## Getting Started

### Accessing the Dashboard

Access the dashboard via your web browser at:

http://[your-server-address]/


No additional software installation is required. The dashboard works best with **Chrome**, **Firefox**, or **Edge** (latest versions).

### User Interface Basics

The dashboard uses a dark theme designed for visibility in security operations environments. The interface includes:

- Top navigation bar  
- Summary cards for key metrics  
- Filtering controls  
- Data visualization charts  
- Detailed data tables  

### Data Refresh

- The dashboard fetches data automatically upon loading.  
- To manually refresh: click the refresh icon in the top-right corner of the nav bar.  
- The **"Last updated"** timestamp will update accordingly.  
- Some elements like risk scores refresh every 5 seconds automatically.  

---

## Dashboard Overview

The dashboard is organized into key sections:

### 1. Summary Cards

At the top of the dashboard:

- **Monitored Assets**: Total number of tracked assets  
- **Active Threats**: Current number of identified threats  
- **High Risk Threats**: Number of threats with "High" risk classification  
- **Mitigation Strategies**: Number of available recommendations  

### 2. Report Generation Controls

Buttons for generating:

- **CSV reports** (for analysis)  
- **PDF reports** (for presentation)  

### 3. Enhanced Filtering Controls

Advanced filters for threats based on:

- Severity  
- Impact  
- Threat type  
- Risk score  

### 4. Data Sections

- **Asset Inventory**  
- **Threat Intelligence Overview**  
- **Risk Trend Analysis**  
- **Threat Distribution**  
- **Threat Data** (network-focused)  
- **Mitigation Strategies**  
- **Real-Time Risk Assessment**  

---

## Monitoring Assets

### Asset Inventory Section

Displays all digital assets under monitoring:

- **Name**: Asset identifier  
- **Type**: Server, DB, network device, etc.  
- **Description**: Detailed info  

### Filtering Assets

- Use **"Filter by Type"** dropdown (top-right of Asset Inventory section)  
- Select asset type → table updates  
- To reset → choose **"All Types"**

### Asset Details

Hover over the description field to expand full asset descriptions.

---

## Analyzing Threats

### Threat Intelligence Overview

Displays detailed threat data:

- **Threat**: Name or description  
- **Vulnerability**: Exploited weakness  
- **Likelihood**: Probability score (1-5)  
- **Impact**: Damage score (1-5)  
- **Risk**: Combined score + classification  

### Threat Data Section

Network-specific threat info:

- **IP Address**: Source/target  
- **Ports**: Open ports detected  
- **Services**: Vulnerable services  

### Visual Analysis Tools

- **Risk Trend Analysis**: Historical chart  
- **Threat Distribution**: Risk level pie chart  
- **Real-Time Risk Assessment**: Bar chart  

---

## Advanced Threat Filtering

### Enhanced Filtering Controls

Filters include:

- **Severity**: High/Medium/Low  
- **Impact**: Level 1–5  
- **Threat Type**: Category-based  
- **Risk Score**: Set minimum threshold  

### Using Filters

- Select values via dropdown/input fields  
- Tables and charts auto-update  
- Active filters show as **chips** below controls  
- Remove filters by clicking the **‘X’** on each chip  

### Filter Results Summary

- Displays number of shown vs. total threats  
- Active filters visible for quick review  

---

## Understanding Risk Scores

### Risk Calculation

```plaintext
Risk Score = Likelihood × 

# ShopSmart Solutions Threat Intelligence Dashboard

## User Guide for Blue Team Analysts  
**Version 1.0**  
**Last Updated: April 11, 2025**

---

## Table of Contents

- [Introduction](#introduction)  
- [Getting Started](#getting-started)  
- [Dashboard Overview](#dashboard-overview)  
- [Monitoring Assets](#monitoring-assets)  
- [Analyzing Threats](#analyzing-threats)  
- [Advanced Threat Filtering](#advanced-threat-filtering)  
- [Understanding Risk Scores](#understanding-risk-scores)  
- [Reviewing Mitigation Strategies](#reviewing-mitigation-strategies)  
- [Generating Reports](#generating-reports)  
- [Best Practices](#best-practices)  
- [Quick Reference](#quick-reference)  

---

## Introduction

Welcome to the **ShopSmart Solutions Threat Intelligence Dashboard** — your central command center for monitoring, analyzing, and responding to security threats across your organization's digital infrastructure.

This user guide is specifically designed for **blue team analysts** and provides practical instructions on using the dashboard effectively to enhance your organization's security posture.

### Purpose of the Dashboard

The dashboard serves as a real-time threat intelligence platform that helps you:

- Monitor all digital assets in your environment  
- Identify and prioritize security threats  
- Understand risk levels and trends  
- Implement effective mitigation strategies  
- Generate comprehensive security reports  

---

## Getting Started

### Accessing the Dashboard

Access the dashboard via your web browser:  
`http://[your-server-address]/`

> **Supported browsers:** Chrome, Firefox, Edge (latest versions)  
> **Note:** No software installation required.

### User Interface Basics

- **Dark theme:** Optimized for SOC environments  
- **Navigation bar:** Top of screen  
- **Summary cards:** Display key metrics  
- **Filters & charts:** Interactive and real-time  
- **Tables:** Detailed data views  

### Data Refresh

- Auto-refresh on load  
- Manual refresh: Click the 🔄 icon (top-right)  
- Risk scores auto-refresh every 5 seconds  

---

## Dashboard Overview

### Key Sections

1. **Summary Cards**  
   - Monitored Assets  
   - Active Threats  
   - High Risk Threats  
   - Mitigation Strategies  

2. **Report Generation Controls**  
   - CSV for analysis  
   - PDF for presentation  

3. **Enhanced Filtering Controls**  
   - Filter by Severity, Impact, Type, Risk Score  

4. **Data Sections**  
   - Asset Inventory  
   - Threat Intelligence  
   - Risk Trends  
   - Threat Distribution  
   - Threat Data  
   - Mitigation Strategies  
   - Real-Time Risk Assessment  

---

## Monitoring Assets

### Asset Inventory Section

Displays all monitored digital assets:

- **Name**  
- **Type** (server, database, etc.)  
- **Description**  

### Filtering Assets

- Use “Filter by Type” dropdown  
- Select a type or choose “All Types” to reset  

### Asset Details

- Hover over the **Description** to view full text  

---

## Analyzing Threats

### Threat Intelligence Overview

Displays identified threat details:

- **Threat**  
- **Vulnerability**  
- **Likelihood** (1–5)  
- **Impact** (1–5)  
- **Risk** (score & classification)  

### Threat Data Section

Focuses on network threat elements:

- **IP Address**  
- **Ports**  
- **Services**  

### Visual Analysis Tools

- **Risk Trend Analysis**  
- **Threat Distribution**  
- **Real-Time Risk Assessment**  

---

## Advanced Threat Filtering

### Enhanced Filtering Controls

Filter threats by:

- **Severity** (Low, Medium, High)  
- **Impact** (1–5)  
- **Threat Type**  
- **Risk Score** (threshold)  

### Using Filters

- Apply filters via dropdown/input  
- View results instantly  
- Active filters appear as **chips**  
- Remove chips with ❌ icon  

### Filter Results Summary

- Shows filtered count vs total  
- Active filters displayed for reference  

---

## Understanding Risk Scores

### Risk Calculation

- **Formula:** `Risk Score = Likelihood × Impact`  
- **Likelihood:** 1–5  
- **Impact:** 1–5  
- **Score Range:** 1–25  

### Risk Classification

- **Low Risk (Green):** 1–9  
- **Medium Risk (Orange):** 10–19  
- **High Risk (Red):** 20–25  

### Risk Visualization

Color-coded consistently:

- **Red → High**  
- **Orange → Medium**  
- **Green → Low**

Appears in:

- Threat Intelligence table (left border)  
- Risk bar chart  
- Pie chart  

---

## Reviewing Mitigation Strategies

### Mitigation Strategies Section

Shows recommendations for threat resolution:

- **Threat Name**  
- **Strategies:** Recommended actions  

### Implementing Mitigations

- **Prioritize by risk score**  
- **Review all suggested strategies**  
- **Follow internal change management**  
- **Document your actions**  
- **Monitor for score changes post-mitigation**  

---

## Generating Reports

### Available Report Types

- **CSV Report:** Raw data  
- **PDF Report:** Formatted visuals  

### Generating a CSV Report

1. Click **Export CSV Report**  
2. Download starts automatically  
3. Open in Excel or similar tool  

### Generating a PDF Report

1. Click **Generate PDF Report**  
2. Download starts automatically  
3. View with any PDF reader  

### Report Contents

- Asset inventory  
- Threat intel data  
- Risk scores  
- Mitigation suggestions  

---

## Best Practices

### Daily Operations

- **Check daily:** Review the dashboard at each shift start  
- **Risk Prioritization:** Address high-risk first  
- **Trend Monitoring:** Watch Risk Trend chart  
- **Action Logging:** Record all mitigations  
- **Weekly Reports:** Share with leadership  

### Incident Response Workflow

- **Assess:** Review new threats  
- **Contextualize:** Identify affected assets  
- **Investigate:** Use network data  
- **Plan:** Review strategies  
- **Act:** Mitigate threats  
- **Document:** Note actions taken  
- **Verify:** Ensure threat reduction  

---

## Quick Reference

| Task | Action |
|------|--------|
| Refresh Data | Click refresh icon (top-right) |
| Filter by Type | Use dropdown in Asset Inventory section |
| View Full Description | Hover over truncated text |
| Export CSV Report | Click Export CSV Report in action bar |
| Export PDF Report | Click Generate PDF Report in action bar |
| Remove Filter | Click ‘X’ on filter chip |
| Identify High Risk Threats | Look for Red highlights in charts and tables |

---

