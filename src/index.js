const express = require('express');
const path = require('path');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.PORT || 3000;

// Rate limiting to prevent abuse
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false,
});

// Middleware
app.use(express.json());
app.use(limiter);
app.use(express.static('public'));

// Basic route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// API endpoint for P2P connection info
app.get('/api/status', (req, res) => {
  res.json({
    status: 'online',
    mode: 'peer-to-peer',
    version: '0.1.0'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`ReadyM Launcher P2P server running on port ${PORT}`);
  console.log(`Access the launcher at http://localhost:${PORT}`);
});
