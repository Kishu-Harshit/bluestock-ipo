const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3001;

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from Node.js backend!' });
});

app.listen(PORT, () => {
  console.log(`Node server running on http://localhost:${PORT}`);
});
