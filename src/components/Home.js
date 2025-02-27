import React from "react";
import { Button, Typography, Container } from "@mui/material";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <Container style={{ textAlign: "center", marginTop: "100px" }}>
      <Typography variant="h3" gutterBottom>
      Real-Time Threat Intelligence
      </Typography>
      <Typography variant="h6" paragraph>
        Please login to access the dashboard.
      </Typography>
      <Button variant="contained" color="primary" component={Link} to="/login">
        Login
      </Button>
    </Container>
  );
};

export default Home;
