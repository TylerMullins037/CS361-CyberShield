# ShopSmart Solutions Threat Intelligence Dashboard
## System Documentation
**Version 1.0**  
**Last Updated: April 11, 2025**

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Technical Requirements](#technical-requirements)
- [Installation & Deployment](#installation--deployment)
- [System Configuration](#system-configuration)
- [API Integration](#api-integration)
- [Data Models](#data-models)
- [Authentication & Authorization](#authentication--authorization)
- [Automated Mitigation System](#automated-mitigation-system)
- [Performance Considerations](#performance-considerations)
- [Maintenance Procedures](#maintenance-procedures)
- [System Logging](#system-logging)
- [Backup & Recovery](#backup--recovery)
- [Security Controls](#security-controls)
- [Technical Troubleshooting](#technical-troubleshooting)

## Architecture Overview
The ShopSmart Solutions Threat Intelligence Dashboard is a web-based application built on a client-server architecture:
- **Frontend**: React.js application with Material-UI components and Recharts for data visualization
- **Backend**: API server (technology not specified in current documentation) that provides data endpoints and report generation capabilities
- **Data Flow**: Frontend makes HTTP requests to backend API endpoints to retrieve security data and initiate reports

### Component Diagram
```
┌─────────────────┐       HTTP       ┌────────────────┐      ┌─────────────┐
│                 │    Requests      │                │      │             │
│  React Frontend ├─────────────────►│  Backend API   │◄─────┤  Data Store │
│                 │                  │                │      │             │
└─────────────────┘                  └────────────────┘      └─────────────┘
         ▲                                   │
         │                                   │
         │           ┌──────────────┐        │
         │           │              │        │
         └───────────┤   Reports    │◄───────┘
                     │              │
                     └──────────────┘
```

## Technical Requirements

### Frontend Requirements
- Node.js: v14.x or higher
- npm: v7.x or higher
- Modern Web Browser: Chrome, Firefox, Edge (latest versions)
- Dependencies:
  - React
  - Material-UI
  - Recharts
  - React Router (if implementing multi-page navigation)

### Backend Requirements
- Web server with API capabilities
- Database for storing security data
- Report generation capabilities (PDF, CSV)
- Network access to monitored assets for data collection
- Dependencies:
  - Ollama
  - Deekseek local model
  - Sklearn
  - requests

### Development Tools
- Git for version control
- Code editor (VS Code recommended)
- React Developer Tools browser extension
- API testing tool (Postman, Insomnia)

## Installation & Deployment

### Frontend Deployment
1. **Clone Repository**:
   ```bash
   git clone https://github.com/TylerMullins037/CS361-CyberShield/tree/main/src/threat-dashboard.git
   cd threat-dashboard
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment**: Create a `.env` file in the project root with the following variables:
   ```
   REACT_APP_API_BASE_URL=http://localhost:5000
   REACT_APP_REFRESH_INTERVAL=5000
   ```

4. **Build for Production**:
   ```bash
   npm run build
   ```

5. **Deploy Build Artifacts**: Deploy the contents of the build directory to your web server.
6. **Server Configuration**: Configure your web server (Apache, Nginx) to serve the static files and handle client-side routing.

### Backend Deployment
- Download and install the app.py file for the backend server
- GET /api/assets - Returns asset inventory
- GET /api/threats - Returns threat intelligence data
- GET /api/threat_data - Returns network vulnerability scan data
- GET /api/mitigation-strategies - Returns recommended mitigation actions
- GET /api/risk-trends - Returns historical risk data
- GET /api/generate-csv-report - Generates and returns CSV report
- GET /api/generate-pdf-report - Generates and returns PDF report

## System Configuration

### Frontend Configuration Options
The dashboard includes several configurable options:

1. **API Endpoints**: Modify the utility functions in the code to point to your API endpoints:
   ```javascript
   const fetchAssets = async () => {
     const response = await fetch("http://your-api-url/api/assets");
     return await response.json();
   };
   ```

2. **Refresh Intervals**: The dashboard refreshes risk scores every 5 seconds. This can be modified in the useEffect hook:
   ```javascript
   useEffect(() => {
     const interval = setInterval(() => {
       // Risk score calculation
     }, 5000); // Change this value to modify refresh interval
     
     return () => clearInterval(interval);
   }, [threats]);
   ```

3. **Theme Customization**: The dashboard uses a dark theme by default. This can be modified in the darkTheme object:
   ```javascript
   const darkTheme = createTheme({
     palette: {
       mode: 'dark', // Change to 'light' for light theme
       primary: {
         main: '#3f51b5', // Change primary color
       },
       // Other theme options
     },
   });
   ```

### Backend Configuration
The backend system should be configured to:
- Collect security data from relevant sources (network scanners, log systems, threat feeds)
- Process and store this data in a structured format
- Expose the data through the required API endpoints
- Implement report generation functionality
- Apply appropriate security controls for API access

## API Integration

### API Endpoints

The frontend expects the following API endpoints:

| Endpoint | Method | Description | Expected Response Format |
|----------|--------|-------------|--------------------------|
| /api/assets | GET | Retrieve asset inventory | Array of asset objects |
| /api/threats | GET | Retrieve threat intelligence | Array of threat objects |
| /api/threat_data | GET | Retrieve network vulnerability data | Array of network data objects |
| /api/mitigation-strategies | GET | Retrieve mitigation recommendations | Array of mitigation objects |
| /api/risk-trends | GET | Retrieve historical risk data | Array of risk trend objects |
| /api/generate-csv-report | GET | Generate CSV report | JSON with file URL |
| /api/generate-pdf-report | GET | Generate PDF report | JSON with file URL |

### Response Object Structures

#### Asset Object
```json
{
  "id": "string",
  "asset_name": "string",
  "asset_type": "string",
  "description": "string"
}
```

#### Threat Object
```json
{
  "name": "string",
  "vulnerability": "string",
  "likelihood": "number (1-5)",
  "impact": "number (1-5)",
  "risk_score": "number (1-25)",
  "type": "string"
}
```

#### Threat Data Object
```json
{
  "ip_address": "string",
  "ports": "array of strings or string",
  "services": "array of strings or string"
}
```

#### Mitigation Object
```json
{
  "threat": "string",
  "strategies": "string or array of strings"
}
```

#### Risk Trend Object
```json
{
  "date": "string (date format)",
  "count": "number"
}
```

#### Report Response
```json
{
  "success": "boolean",
  "file": "string (file path)",
  "error": "string (optional)"
}
```

## Data Models

The following data models are used in the application:

### Asset Model
- Asset ID (unique identifier)
- Asset Name
- Asset Type (server, database, network device, etc.)
- Description

### Threat Model
- Threat Name
- Vulnerability Description
- Likelihood (1-5 scale)
- Impact (1-5 scale)
- Risk Score (calculated as likelihood × impact)
- Threat Type (category)

### Threat Data Model
- IP Address
- Ports (open ports)
- Services (running services)

### Mitigation Model
- Associated Threat
- Mitigation Strategies (single or multiple)

### Risk Trend Model
- Date
- Threat Count

## Automated Mitigation System

The threat intelligence dashboard includes an AI-powered automated mitigation system that provides recommendations for addressing identified threats. This section details the technical implementation and configuration of this system.

### Architecture Overview

The automated mitigation system follows this architecture:

```
┌───────────────┐     ┌───────────────────┐     ┌────────────────────┐
│               │     │                   │     │                    │
│  PostgreSQL   │────►│  Python-based     │────►│  LLM-powered       │
│  Database     │     │  Recommendation   │     │  Mitigation        │
│               │     │  Engine           │     │  Generator         │
└───────────────┘     └───────────────────┘     └────────────────────┘
                              │                           │
                              ▼                           ▼
                      ┌───────────────────┐     ┌────────────────────┐
                      │                   │     │                    │
                      │  Threat-to-Asset  │     │  Mitigation        │
                      │  Mapping Table    │     │  Strategies Table  │
                      │                   │     │                    │
                      └───────────────────┘     └────────────────────┘
```

### Key Components

- **PostgreSQL Database**:
  - Stores threat data, asset mappings, and mitigation strategies
  - Connected via psycopg2 PostgreSQL adapter

- **Python Recommendation Engine**:
  - Fetches threat data from the database
  - Coordinates the AI-based recommendation generation
  - Updates the database with new mitigation strategies

- **LLM-powered Mitigation Generator**:
  - Uses the Ollama API to interact with "deepseek-r1:1.5b" model
  - Analyzes threats and generates specific mitigation recommendations
  - Structures responses in a standardized format

- **Database Schema**:
  - tva_mapping table: Maps threats to vulnerable assets
  - mitigation_strategies table: Stores generated mitigation recommendations

### Implementation Details

#### Database Connection

The system connects to a PostgreSQL database hosted on DigitalOcean:

```python
def get_db_connection():
    return psycopg2.connect(
        dbname="defaultdb",
        user="doadmin",
        password="*******",
        host="db-postgresql-nyc3-21525-do-user-20065838-0.k.db.ondigitalocean.com",
        port="25060"
    )
```

#### Threat Data Retrieval

The system fetches threat data from the tva_mapping table:

```python
def fetch_threat_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, asset_id, threat_name, vulnerability_description FROM tva_mapping;")
    threats = cursor.fetchall()
    conn.close()
    return threats
```

#### AI-powered Mitigation Recommendation

The system leverages the Ollama API to generate mitigation recommendations:

```python
async def mitigation_recommendation(threat_description):
    try:
        response = chat(model='deepseek-r1:1.5b', messages=[{
            'role': 'system',
            'content': f"""
            You are an expert in cybersecurity analysis. Please evaluate the following threat description 
            based on current industry trends and standards. For the given threat, provide ONLY ONE 
            recommended mitigation strategies to reduce or eliminate the risk associated with it.
            Your recommendations should focus on practical, actionable measures such as security controls,
            best practices, or industry standards. Consider factors such as the latest security frameworks,
            attack vectors, and relevant technology.
            Please respond strictly in the following format: 'Mitigation Strategies: [one strategy]''
            where the strategies are specific, clear, and focused on actionable solutions.
            Threat: {threat_description}
            """
        }])
        
        # Extract mitigation strategies from the response
        response_content = response.get('message', {}).get('content', '')
        match = re.search(r"Mitigation Strategies:\s*(.*)", response_content, re.DOTALL)
        if match:
            mitigation_strategies = match.group(1).strip()
            return mitigation_strategies
        else:
            return "No Available Mitigation Recommendations"
    except Exception as e:
        print(f"Error during mitigation extraction: {e}")
        return "No Available Mitigation Recommendations"
```

#### Update Process

The system updates the mitigation recommendations through an async process:

```python
async def update_recommendations():
    threats = fetch_threat_data()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for tva_id, asset_id, threat_name, vulnerability_description in threats:
        threat_description = threat_name + " " + vulnerability_description
        recommendation = await mitigation_recommendation(threat_description)
        
        cursor.execute(
            """
            INSERT INTO public.mitigation_strategies (tva_mapping_id, mitigation_strategy) 
            VALUES (%s, %s);
            """,
            (tva_id, recommendation)
        )
    
    conn.commit()
    conn.close()
```

#### Deployment and Execution

The system is designed to be run as a scheduled task or service:

```python
if __name__ == "__main__":
    asyncio.run(update_recommendations())
```

This can be configured to run at regular intervals using cron jobs or a similar scheduling mechanism.

### Dependencies and Requirements

The automated mitigation system requires:

- **Python Libraries**:
  - asyncio: For asynchronous operations
  - psycopg2: PostgreSQL database adapter
  - ollama: Client for the Ollama API

- **External Services**:
  - PostgreSQL database (hosted on DigitalOcean)
  - Ollama API with access to the deepseek-r1:1.5b model

### Integration with the Dashboard

The mitigation strategies generated by this system are displayed in the dashboard's "Mitigation Strategies" section. The React frontend fetches these recommendations through the `/api/mitigation-strategies` endpoint.

### Configuration Considerations

When deploying this automated mitigation system:

#### Security Considerations:
- Store database credentials securely (consider using environment variables)
- Implement proper authentication for the Ollama API
- Review and audit generated recommendations before automated implementation

#### Performance Optimization:
- Implement caching for frequently accessed threat data
- Consider batching database operations for efficiency
- Implement rate limiting for the LLM API calls

#### Maintenance Requirements:
- Regularly update the LLM model for improved recommendations
- Monitor recommendation quality and adjust the prompt as needed
- Implement logging for troubleshooting

#### Scalability Planning:
- Consider parallel processing for handling large volumes of threats
- Implement database connection pooling
- Consider distributed architecture for high-availability deployments

### Monitoring and Improvement

To ensure optimal performance:

#### Log Analysis:
- Track recommendation generation success/failure rates
- Monitor database query performance
- Analyze LLM response times

#### Quality Assessment:
- Periodically review generated recommendations for accuracy
- Gather feedback from security analysts on recommendation quality
- Refine the LLM prompt based on real-world effectiveness

#### Exception Handling:
- Implement comprehensive error handling
- Set up alerts for persistent failures
- Create fallback mechanisms for when the LLM service is unavailable

## Performance Considerations

### Frontend Optimizations
- **Data Pagination**: For large datasets, implement pagination in the tables
- **Lazy Loading**: Load components and data only when needed
- **Memoization**: Use React.memo and useMemo for expensive calculations
- **Bundle Optimization**: Split code into smaller chunks

### Backend Optimizations
- **Data Caching**: Cache frequently accessed data
- **Query Optimization**: Optimize database queries
- **Rate Limiting**: Implement API rate limiting
- **Response Compression**: Enable GZIP compression for API responses

## Maintenance Procedures

### Regular Maintenance Tasks

#### Dependency Updates:
```bash
npm outdated   # Check for outdated packages
npm update     # Update packages to latest compatible versions
```

#### Performance Monitoring:
- Monitor API response times
- Check for memory leaks in the frontend application
- Monitor browser console for errors

#### Data Cleanup:
- Archive old threat data
- Remove obsolete assets
- Optimize database storage

### Version Upgrades
1. Create a backup of the current system
2. Deploy the new version to a staging environment
3. Perform thorough testing
4. Schedule maintenance window for production upgrade
5. Deploy to production
6. Verify functionality after upgrade

## System Logging

Implement comprehensive logging for both frontend and backend:

### Frontend Logging
- Add error boundary components to catch and log React errors
- Implement analytics tracking for user interactions
- Log performance metrics (load times, rendering times)

### Backend Logging
- Log all API requests and responses
- Log authentication events
- Log system errors and exceptions
- Log performance metrics

### Log Storage and Analysis
- Centralize logs in a log management system
- Implement log rotation and retention policies
- Set up alerts for critical errors
- Regularly review logs for security incidents

## Backup & Recovery

### Backup Procedures

#### Database Backup:
- Schedule regular backups of the security data
- Store backups securely and off-site

#### Application Backup:
- Maintain versioned backups of application code
- Document configuration settings

### Recovery Procedures

#### Database Recovery:
- Restore from latest backup
- Verify data integrity

#### Application Recovery:
- Deploy from backup code repository
- Apply configuration settings
- Verify functionality

## Security Controls

### Application Security
- **Input Validation**: Validate all user inputs
- **Output Encoding**: Encode all outputs to prevent XSS
- **CSRF Protection**: Implement Cross-Site Request Forgery protection
- **Content Security Policy**: Implement strict CSP headers

### Infrastructure Security
- **Firewall Rules**: Restrict access to API servers
- **Network Segmentation**: Isolate security monitoring systems
- **Vulnerability Scanning**: Regularly scan infrastructure
- **Patch Management**: Keep all systems updated

### Data Security
- **Encryption**: Encrypt sensitive data at rest and in transit
- **Access Controls**: Implement least privilege access
- **Data Classification**: Classify and handle data according to sensitivity
- **Data Retention**: Implement appropriate data retention policies

## Technical Troubleshooting

### Common Issues and Solutions

#### API Connection Failures:
- Check network connectivity
- Verify API server is running
- Check for CORS issues
- Verify API endpoints are correctly configured

#### Dashboard Loading Issues:
- Check browser console for JavaScript errors
- Verify all required assets are loaded
- Check for compatibility issues with browser

#### Data Visualization Problems:
- Verify data format matches expected format
- Check for null or undefined values in the data
- Verify chart configuration

#### Performance Issues:
- Check for memory leaks
- Monitor API response times
- Optimize rendering of large datasets

### Diagnostic Tools

#### Network Monitoring:
- Browser Network tab
- API testing tools (Postman, Insomnia)

#### Performance Profiling:
- React Profiler
- Browser Performance tools

#### Error Logging:
- Browser console
- Centralized error logging system

### Component Reference

#### Major Components
- **App Bar**: Navigation and refresh controls
- **Overview Cards**: Summary statistics
- **Enhanced Filtering**: Controls for filtering threat data
- **Asset Inventory**: Table of monitored assets
- **Threat Intelligence**: Table of active threats
- **Risk Trend Analysis**: Historical risk data chart
- **Threat Distribution**: Pie chart of risk levels
- **Threat Data**: Network vulnerability data
- **Mitigation Strategies**: Recommended security actions
- **Risk Assessment Chart**: Bar chart of risk scores
