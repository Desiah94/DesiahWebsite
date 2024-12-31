const express = require('express');
const cors = require('cors');
const path = require('path');
const mongoose = require('mongoose');
const Message = require('./models/Message');  // Import the Mongoose model

const app = express();
const PORT = 3000;

// Use CORS middleware
app.use(cors());

// Parse JSON request bodies
app.use(express.json());

// Serve static files
app.use(express.static(path.join(__dirname, 'portfolio-responsive-complete')));

// MongoDB connection URI (local or MongoDB Atlas URI)
const mongoURI = 'mongodb://localhost:27017/contact-form';  // Use MongoDB URI
// For MongoDB Atlas, use the connection string from your Atlas dashboard
// const mongoURI = 'your-atlas-uri';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch((err) => console.error('Error connecting to MongoDB:', err));

// Handle contact form submission
app.post('/api/contact', async (req, res) => {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        // Create a new Message instance
        const newMessage = new Message({ name, email, message });

        // Save the message to MongoDB
        await newMessage.save();

        res.status(200).json({ success: 'Message received successfully!' });
    } catch (error) {
        console.error('Error saving message:', error);
        res.status(500).json({ error: 'Failed to save the message.' });
    }
});

// Serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'portfolio-responsive-complete', 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
