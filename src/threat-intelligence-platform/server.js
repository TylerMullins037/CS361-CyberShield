// Import required modules
const express = require("express");
const axios = require("axios");
require("dotenv").config();
const cors = require("cors");

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json()); // Parse JSON requests
app.use(cors()); // Enable CORS

// Default Route
app.get("/", (req, res) => {
    res.send("Threat Intelligence Platform API is running.");
});

// Example OSINT API Route
app.get("/osint", async (req, res) => {
    try {
        const response = await axios.get("https://api.example.com/osint"); // Replace with real OSINT API URL
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Error fetching OSINT data" });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
