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

// Function to fetch assets from your server
const fetchAssets = async () => {
  const response = await fetch("http://localhost:5000/api/assets");
  const data = await response.json();
  return data;
};

// Function to fetch threats from your server
const fetchThreats = async () => {
  const response = await fetch("http://localhost:5000/api/threats");
  const data = await response.json();
  return data;
};

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
  const [assets, setAssets] = useState([]);
  const [threats, setThreats] = useState([]);
  const [riskScores, setRiskScores] = useState([]);

  useEffect(() => {
    // Fetch the data when the component mounts
    const fetchData = async () => {
      const fetchedAssets = await fetchAssets();
      const fetchedThreats = await fetchThreats();

      setAssets(fetchedAssets);
      setThreats(fetchedThreats);
    };

    fetchData();
  }, []);

  useEffect(() => {
    // Simulate dynamic real-time risk scores update
    const interval = setInterval(() => {
      const newRiskScores = assets.map((asset) => ({
        asset: asset.asset_name,
        risk: Math.floor(Math.random() * 25),
      }));
      setRiskScores(newRiskScores);
    }, 5000);

    return () => clearInterval(interval);
  }, [assets]);

  return (
    <Grid container spacing={3} sx={{ p: 3, backgroundColor: "#A9A9A9" }}>
      {/* Asset Inventory */}
      <Grid item xs={12} md={6}>
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Asset Inventory
            </Typography>
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell><strong>Name</strong></TableCell>
                    <TableCell><strong>Type</strong></TableCell>
                    <TableCell><strong>Description</strong></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {assets.map((asset) => (
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
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Threat Intelligence Overview
            </Typography>
            <ThreatList threats={threats} />
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



        </Card>
      </Grid>
    </Grid>
  );
}

