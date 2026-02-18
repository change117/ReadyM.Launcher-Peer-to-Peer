const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
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
