import React from "react";
import { Container, Button } from "@mui/material";
import "./dashboard.css"; // Import the CSS file

const Dashboard = () => {
  return (
    <Container className="dashboard-container">
      <div className="dashboard-header">
        <h2>Threat Intelligence Dashboard</h2>
      </div>

      <div className="dashboard-card">
        <h3 className="card-title">Threat Logs</h3>
        <div className="card-content">
          <p>View the latest threat logs and incidents.</p>
        </div>
        <Button className="card-button">View Logs</Button>
      </div>

      <div className="dashboard-card">
        <h3 className="card-title">Risk Scores</h3>
        <div className="card-content">
          <p>Monitor the current risk scores based on the latest data.</p>
        </div>
        <Button className="card-button">View Scores</Button>
      </div>

      <div className="dashboard-card">
        <h3 className="card-title">Real-time Alerts</h3>
        <div className="card-content">
          <p>Stay updated with real-time security alerts.</p>
        </div>
        <Button className="card-button">View Alerts</Button>
      </div>
    </Container>
  );
};

export default Dashboard;

