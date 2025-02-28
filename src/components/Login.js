import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Container, TextField, Button, Typography, Card, CardContent } from "@mui/material";
import { useAuth } from "../AuthContext";

const Login = () => {
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    // Mock authentication (Replace with real authentication logic)
    if (username === "admin" && password === "password") {
      login(); // Set authentication state
      navigate("/dashboard"); // Redirect to Dashboard
    } else {
      setError("Invalid username or password.");
    }
  };

  return (
    <Container maxWidth="sm" style={{ marginTop: "50px" }}>
      <Card>
        <CardContent>
          <Typography variant="h5" gutterBottom>
            Login
          </Typography>

          {error && <Typography color="error">{error}</Typography>}

          <TextField
            fullWidth
            label="Username"
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <TextField
            fullWidth
            label="Password"
            type="password"
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <Button
            variant="contained"
            color="primary"
            fullWidth
            onClick={handleLogin}
            style={{ marginTop: "15px" }}
          >
            Login
          </Button>
        </CardContent>
      </Card>
    </Container>
  );
};

export default Login;
