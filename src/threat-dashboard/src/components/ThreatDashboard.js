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
  TextField,
  MenuItem,
} from "@mui/material";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const fetchAssets = async () => {
  const response = await fetch("http://localhost:5000/api/assets");
  return await response.json();
};

const fetchThreats = async () => {
  const response = await fetch("http://localhost:5000/api/threats");
  return await response.json();
};

const fetchThreatData = async () => {
  const response = await fetch("http://localhost:5000/api/threat_data");
  return await response.json();
};

export default function ThreatDashboard() {
  const [assets, setAssets] = useState([]);
  const [threats, setThreats] = useState([]);
  const [threatData, setThreatData] = useState([]);
  const [riskScores, setRiskScores] = useState([]);
  const [filterType, setFilterType] = useState("");
  const [filterRisk, setFilterRisk] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      setAssets(await fetchAssets());
      setThreats(await fetchThreats());
      setThreatData(await fetchThreatData());
    };
    fetchData();
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setRiskScores(
        assets.map((asset) => ({
          asset: asset.asset_name,
          risk: Math.floor(Math.random() * 25),
        }))
      );
    }, 5000);
    return () => clearInterval(interval);
  }, [assets]);

  const filteredAssets = assets.filter((asset) => !filterType || asset.asset_type === filterType);
  const filteredThreats = threats.filter((threat) => !filterRisk || threat.risk_score >= filterRisk);

  return (
    <Grid container spacing={3} sx={{ p: 3, backgroundColor: "#A9A9A9" }}>
      <Grid item xs={12} md={6}>
        <TextField
          select
          label="Filter by Asset Type"
          value={filterType}
          onChange={(e) => setFilterType(e.target.value)}
          fullWidth
          variant="outlined"
          sx={{ mb: 2 }}
        >
          <MenuItem value="">All</MenuItem>
          {[...new Set(assets.map((a) => a.asset_type))].map((type) => (
            <MenuItem key={type} value={type}>{type}</MenuItem>
          ))}
        </TextField>
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
                  {filteredAssets.map((asset) => (
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

      <Grid item xs={12} md={6}>
        <TextField
          label="Filter by Risk Score (>=)"
          type="number"
          value={filterRisk}
          onChange={(e) => setFilterRisk(e.target.value)}
          fullWidth
          variant="outlined"
          sx={{ mb: 2 }}
        />
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Threat Intelligence Overview
            </Typography>
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell><strong>Threat</strong></TableCell>
                    <TableCell><strong>Vulnerability</strong></TableCell>
                    <TableCell><strong>Likelihood</strong></TableCell>
                    <TableCell><strong>Impact</strong></TableCell>
                    <TableCell><strong>Risk Score</strong></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {filteredThreats.map((threat, index) => (
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
          </CardContent>
        </Card>
      </Grid>


      <Grid container spacing={3} sx={{ p: 3, backgroundColor: "#A9A9A9" }}>

      {/* Threat Data */}
      <Grid item xs={12} md={6}>
        <Card sx={{ boxShadow: 3, backgroundColor: "#22303c" }}>
          <CardContent>
            <Typography variant="h6" gutterBottom sx={{ color: "#ffffff" }}>
              Threat Data
            </Typography>
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell><strong>IP Address</strong></TableCell>
                    <TableCell><strong>Ports</strong></TableCell>
                    <TableCell><strong>Services</strong></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {threatData.map((threats_data, id) => (
                    <TableRow key={id}>
                      <TableCell>{threats_data.ip_address}</TableCell>
                      <TableCell>{Array.isArray(threats_data.ports) ? threats_data.ports.join(" / ") : threats_data.ports}
                      </TableCell>
                      <TableCell>{Array.isArray(threats_data.services) ? threats_data.services.join(" / ") : threats_data.services}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </CardContent>
        </Card>
      </Grid>
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



    </Grid>
  );
}

