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
  Box,
  Chip,
  AppBar,
  Toolbar,
  IconButton,
  Container,
  Divider,
  Alert,
  useTheme,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from "@mui/material";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Cell } from "recharts";
import SecurityIcon from '@mui/icons-material/Security';
import RefreshIcon from '@mui/icons-material/Refresh';
import WarningIcon from '@mui/icons-material/Warning';
import DashboardIcon from '@mui/icons-material/Dashboard';
import StorageIcon from '@mui/icons-material/Storage';
import ShieldIcon from '@mui/icons-material/Shield';

// Custom theme
const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#3f51b5',
    },
    secondary: {
      main: '#f50057',
    },
    background: {
      default: '#121212',
      paper: '#1e1e1e',
    },
    error: {
      main: '#f44336',
    },
    warning: {
      main: '#ff9800',
    },
    info: {
      main: '#2196f3',
    },
    success: {
      main: '#4caf50',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h5: {
      fontWeight: 600,
    },
    h6: {
      fontWeight: 500,
    },
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          boxShadow: '0 4px 20px 0 rgba(0,0,0,0.12)',
        },
      },
    },
    MuiTableCell: {
      styleOverrides: {
        head: {
          backgroundColor: '#2c2c2c',
          color: '#fff',
          fontWeight: 600,
        },
      },
    },
  },
});

// Utility functions for API calls
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

const fetchMitigations = async () => {
  const response = await fetch("http://localhost:5000/api/mitigation-strategies");
  return await response.json();
};

// Risk score color mapping
const getRiskColor = (score) => {
  if (score >= 20) return '#f44336'; // High risk - red
  if (score >= 10) return '#ff9800'; // Medium risk - orange
  return '#4caf50'; // Low risk - green
};

// Convert risk score to text
const getRiskLevel = (score) => {
  if (score >= 20) return 'High';
  if (score >= 10) return 'Medium';
  return 'Low';
};

export default function ThreatDashboard() {
  const [assets, setAssets] = useState([]);
  const [threats, setThreats] = useState([]);
  const [threatData, setThreatData] = useState([]);
  const [riskScores, setRiskScores] = useState([]);
  const [mitigations, setMitigations] = useState([]);
  const [filterType, setFilterType] = useState("");
  const [filterRisk, setFilterRisk] = useState("");
  const [loading, setLoading] = useState(true);
  const [lastUpdated, setLastUpdated] = useState(new Date());

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const assetsData = await fetchAssets();
        const threatsData = await fetchThreats();
        const threatDataResults = await fetchThreatData();
        const mitigationsData = await fetchMitigations();
        
        setAssets(assetsData);
        setThreats(threatsData);
        setThreatData(threatDataResults);
        setMitigations(mitigationsData);
        setLastUpdated(new Date());
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setRiskScores(
        threats.map((threat) => ({
          threat: threat.name,
          risk: threat.risk_score,
          color: getRiskColor(threat.risk_score)
        }))
      );
    }, 5000);
    
    return () => clearInterval(interval);
  }, [threats]);

  const handleRefresh = async () => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setAssets(await fetchAssets());
        setThreats(await fetchThreats());
        setThreatData(await fetchThreatData());
        setMitigations(await fetchMitigations());
        setLastUpdated(new Date());
      } catch (error) {
        console.error("Error refreshing data:", error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  };

  const filteredAssets = assets.filter((asset) => !filterType || asset.asset_type === filterType);
  const filteredThreats = threats.filter((threat) => !filterRisk || threat.risk_score >= filterRisk);

  // Get high risk threats count
  const highRiskCount = threats.filter(threat => threat.risk_score >= 20).length;

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <SecurityIcon sx={{ mr: 2 }} />
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              ShopSmart Solutions Dashboard
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <Typography variant="body2" sx={{ mr: 2 }}>
                Last updated: {lastUpdated.toLocaleTimeString()}
              </Typography>
              <IconButton color="inherit" onClick={handleRefresh}>
                <RefreshIcon />
              </IconButton>
            </Box>
          </Toolbar>
        </AppBar>
        
        <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
          {/* Overview Cards */}
          <Grid container spacing={3} sx={{ mb: 4 }}>
            <Grid item xs={12} md={3}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <StorageIcon sx={{ fontSize: 40, color: 'primary.main' }} />
                  <Typography variant="h5" component="div">
                    {assets.length}
                  </Typography>
                  <Typography color="text.secondary">
                    Monitored Assets
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <WarningIcon sx={{ fontSize: 40, color: 'warning.main' }} />
                  <Typography variant="h5" component="div">
                    {threats.length}
                  </Typography>
                  <Typography color="text.secondary">
                    Active Threats
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <ShieldIcon sx={{ fontSize: 40, color: 'error.main' }} />
                  <Typography variant="h5" component="div">
                    {highRiskCount}
                  </Typography>
                  <Typography color="text.secondary">
                    High Risk Threats
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <DashboardIcon sx={{ fontSize: 40, color: 'success.main' }} />
                  <Typography variant="h5" component="div">
                    {mitigations.length}
                  </Typography>
                  <Typography color="text.secondary">
                    Mitigation Strategies
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>

          {/* Main Dashboard */}
          <Grid container spacing={3}>
            {/* Asset Inventory */}
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                    <Typography variant="h6" component="div">
                      Asset Inventory
                    </Typography>
                    <TextField
                      select
                      label="Filter by Type"
                      value={filterType}
                      onChange={(e) => setFilterType(e.target.value)}
                      variant="outlined"
                      size="small"
                      sx={{ width: 200 }}
                    >
                      <MenuItem value="">All Types</MenuItem>
                      {[...new Set(assets.map((a) => a.asset_type))].map((type) => (
                        <MenuItem key={type} value={type}>{type}</MenuItem>
                      ))}
                    </TextField>
                  </Box>
                  <Divider sx={{ mb: 2 }} />
                  <TableContainer component={Paper} elevation={0}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>Name</TableCell>
                          <TableCell>Type</TableCell>
                          <TableCell>Description</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {filteredAssets.map((asset) => (
                          <TableRow key={asset.id}>
                            <TableCell>{asset.asset_name}</TableCell>
                            <TableCell>
                              <Chip 
                                label={asset.asset_type} 
                                size="small" 
                                color="primary" 
                                variant="outlined" 
                              />
                            </TableCell>
                            <TableCell>{asset.description}</TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </CardContent>
              </Card>
            </Grid>

            {/* Threat Intelligence */}
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                    <Typography variant="h6" component="div">
                      Threat Intelligence Overview
                    </Typography>
                    <TextField
                      label="Min Risk Score"
                      type="number"
                      value={filterRisk}
                      onChange={(e) => setFilterRisk(e.target.value)}
                      size="small"
                      sx={{ width: 150 }}
                    />
                  </Box>
                  <Divider sx={{ mb: 2 }} />
                  <TableContainer component={Paper} elevation={0}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>Threat</TableCell>
                          <TableCell>Vulnerability</TableCell>
                          <TableCell align="center">Likelihood</TableCell>
                          <TableCell align="center">Impact</TableCell>
                          <TableCell align="center">Risk</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {filteredThreats.map((threat, index) => (
                          <TableRow key={index}>
                            <TableCell>{threat.name}</TableCell>
                            <TableCell>{threat.vulnerability}</TableCell>
                            <TableCell align="center">{threat.likelihood}/10</TableCell>
                            <TableCell align="center">{threat.impact}/10</TableCell>
                            <TableCell align="center">
                              <Chip 
                                label={`${threat.risk_score} - ${getRiskLevel(threat.risk_score)}`} 
                                size="small" 
                                sx={{ 
                                  bgcolor: getRiskColor(threat.risk_score),
                                  color: 'white',
                                  fontWeight: 'bold' 
                                }} 
                              />
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </CardContent>
              </Card>
            </Grid>

            {/* Threat Data */}
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" component="div" sx={{ mb: 2 }}>
                    Threat Data
                  </Typography>
                  <Divider sx={{ mb: 2 }} />
                  <TableContainer component={Paper} elevation={0}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>IP Address</TableCell>
                          <TableCell>Ports</TableCell>
                          <TableCell>Services</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {threatData.map((threats_data, id) => (
                          <TableRow key={id}>
                            <TableCell>{threats_data.ip_address}</TableCell>
                            <TableCell>
                              {Array.isArray(threats_data.ports) ? 
                                threats_data.ports.map((port, i) => (
                                  <Chip 
                                    key={i}
                                    label={port} 
                                    size="small" 
                                    sx={{ mr: 0.5, mb: 0.5 }} 
                                  />
                                )) : 
                                threats_data.ports
                              }
                            </TableCell>
                            <TableCell>
                              {Array.isArray(threats_data.services) ? 
                                threats_data.services.map((service, i) => (
                                  <Chip 
                                    key={i}
                                    label={service} 
                                    size="small" 
                                    color="info"
                                    variant="outlined"
                                    sx={{ mr: 0.5, mb: 0.5 }} 
                                  />
                                )) : 
                                threats_data.services
                              }
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </CardContent>
              </Card>
            </Grid>

            {/* Mitigation Strategies */}
            <Grid item xs={12} md={6}>
              <Card>
                <CardContent>
                  <Typography variant="h6" component="div" sx={{ mb: 2 }}>
                    Mitigation Strategies
                  </Typography>
                  <Divider sx={{ mb: 2 }} />
                  <TableContainer component={Paper} elevation={0}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>Threat</TableCell>
                          <TableCell>Strategies</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {mitigations.map((mit, id) => (
                          <TableRow key={id}>
                            <TableCell>{mit.threat}</TableCell>
                            <TableCell>
                              {typeof mit.strategies === 'string' ? 
                                mit.strategies : 
                                Array.isArray(mit.strategies) ? 
                                  mit.strategies.map((strategy, i) => (
                                    <Alert 
                                      key={i} 
                                      severity="info" 
                                      icon={<ShieldIcon />}
                                      sx={{ mb: 1 }}
                                    >
                                      {strategy}
                                    </Alert>
                                  )) : 
                                  null
                              }
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </CardContent>
              </Card>
            </Grid>

            {/* Risk Scores Chart */}
            <Grid item xs={12}>
              <Card>
                <CardContent>
                  <Typography variant="h6" component="div" sx={{ mb: 2 }}>
                    Real-Time Risk Assessment
                  </Typography>
                  <Divider sx={{ mb: 2 }} />
                  <Box sx={{ height: 350 }}>
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart 
                        data={riskScores}
                        margin={{ top: 20, right: 30, left: 20, bottom: 70 }}
                      >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis 
                          dataKey="threat" 
                          angle={-45} 
                          textAnchor="end" 
                          height={70} 
                        />
                        <YAxis domain={[0, 25]} />
                        <Tooltip 
                          formatter={(value) => [`Risk Score: ${value}`, 'Risk Level']}
                          labelFormatter={(label) => `Threat: ${label}`}
                        />
                        <Bar 
                          dataKey="risk" 
                          name="Risk Score"
                          fill="#8884d8" 
                          radius={[4, 4, 0, 0]}
                        >
                          {riskScores.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={entry.color || '#8884d8'} />
                          ))}
                        </Bar>
                      </BarChart>
                    </ResponsiveContainer>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </ThemeProvider>
  );
}
