const express = require('express');
const cors = require('cors');
const path = require('path');
const mongoose = require('mongoose');
const Message = require('./models/Message');  // Import the Mongoose model

const app = express();
const port = process.env.PORT || 3000;

// Allow CORS for specific origins (localhost for local dev and your Heroku domain)
const corsOptions = {
    origin: ['http://localhost:3000', 'https://your-heroku-app.herokuapp.com'],
    methods: ['GET', 'POST', 'OPTIONS'],  // Allow OPTIONS method
    credentials: true
};

// Use CORS middleware with the specified options
app.use(cors(corsOptions));

// Parse JSON request bodies
app.use(express.json());

// Serve static files
app.use(express.static(path.join(__dirname, '..', 'portfolio-responsive-complete')));

// MongoDB connection URI (use environment variable for Heroku, fallback to local MongoDB if not set)
const mongoURI = process.env.MONGO_URI || 'mongodb+srv://desiahbarnett:cora1951@cluster0.tsucj.mongodb.net/contact-form?retryWrites=true&w=majority';

// Connect to MongoDB
mongoose.connect(mongoURI)
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Handle contact form submission
app.post('/api/contact', async (req, res) => {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        const newMessage = new Message({ name, email, message });
        await newMessage.save();
        res.status(200).json({ success: 'Message received successfully!' });
    } catch (error) {
        console.error('Error saving message:', error);
        res.status(500).json({ error: 'Failed to save the message.' });
    }
});

// Serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'portfolio-responsive-complete', 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
