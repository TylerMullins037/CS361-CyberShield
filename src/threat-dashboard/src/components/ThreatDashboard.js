import { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Grid,
} from "@mui/material";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

// Sample data for Asset Inventory (WILL CHANGE ONCE DATABASE IS FULLY INTEGRATED)
const mockAssets = [
  { id: 1, asset_name: "Web Server", asset_type: "Software", description: "A software-based server that hosts web applications and services, currently in active operation." },
  { id: 2, asset_name: "Database", asset_type: "Software", description: "A software system used for storing and managing structured data, actively running." },
  { id: 3, asset_name: "Workstation", asset_type: "Hardware", description: "A physical computing device used by employees, currently identified as vulnerable to security threats." },
];

// Sample data for Threat-Vulnerability Mappings with risk scores
const mockThreats = [
  { name: "SQL Injection", vulnerability: "Unpatched Database", likelihood: 4, impact: 5, risk_score: 20 },
  { name: "Phishing", vulnerability: "Weak Employee Awareness", likelihood: 5, impact: 4, risk_score: 20 },
  { name: "Ransomware", vulnerability: "Outdated Backup Policies", likelihood: 3, impact: 4, risk_score: 12 },
];

// Function to simulate dynamic real-time risk scores update
const generateRiskScores = () => {
  return mockAssets.map((asset) => ({
    asset: asset.name,
    risk: Math.floor(Math.random() * 25),
  }));
};

// Threat List Component
function ThreatList({ threats }) {
  return (
    <TableContainer component={Paper} sx={{ mt: 2 }}>
      <Table>
        <TableHead>
          <TableRow sx={{ backgroundColor: "#f5f5f5" }}>
            <TableCell><strong>Threat</strong></TableCell>
            <TableCell><strong>Vulnerability</strong></TableCell>
            <TableCell><strong>Likelihood</strong></TableCell>
            <TableCell><strong>Impact</strong></TableCell>
            <TableCell><strong>Risk Score</strong></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {threats.map((threat, index) => (
            <TableRow key={index}>
              <TableCell>{threat.name}</TableCell>
              <TableCell>{threat.vulnerability}</TableCell>
              <TableCell>{threat.likelihood}</TableCell>
              <TableCell>{threat.impact}</TableCell>
              <TableCell>{threat.risk_score}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default function ThreatDashboard() {
  const [riskScores, setRiskScores] = useState(generateRiskScores());

  useEffect(() => {
    const interval = setInterval(() => {
      setRiskScores(generateRiskScores());
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Grid container spacing={3} sx={{ p: 3, backgroundColor: "#A9A9A9"}}>
      {/* Asset Inventory */}
      <Grid item xs={12} md={6}>
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Asset Inventory
            </Typography>
            <TableContainer component={Paper} >
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell><strong>Name</strong></TableCell>
                    <TableCell><strong>Type</strong></TableCell>
                    <TableCell><strong>Description</strong></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {mockAssets.map((asset) => (
                    <TableRow key={asset.id}>
                      <TableCell>{asset.asset_name}</TableCell>
                      <TableCell>{asset.asset_type}</TableCell>
                      <TableCell>{asset.description}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </CardContent>
        </Card>
      </Grid>

      {/* Threat-Vulnerability Mappings & Risk Scores */}
      <Grid item xs={12} md={6}>
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }} >
              Threat Intelligence Overview
            </Typography>
            <ThreatList threats={mockThreats} />
          </CardContent>
        </Card>
      </Grid>

      {/* Real-Time Risk Scores */}
      <Grid item xs={12}>
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Real-Time Risk Scores
            </Typography>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={riskScores}>
                <XAxis dataKey="asset" />
                <YAxis domain={[0, 25]} />
                <Tooltip />
                <Bar dataKey="risk" fill="#f43f5e" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
}

