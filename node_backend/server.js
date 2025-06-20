const express = require('express');
const cors = require('cors');
const axios = require('axios');
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

app.post('/api/from-django', (req, res) => {
  console.log("Received from Django:", req.body);
  res.json({ msg: "Hi Django, Node.js got your message!", received: req.body });
});

app.get('/call-django', async (req, res) => {
  try {
    const response = await axios.post('http://localhost:8000/api/from-node/', {
      name: "Node.js",
      message: "Hello from Node!"
    });
    res.json(response.data);
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: "Failed to call Django" });
  }
});