// Import dependencies
const express = require('express');
const cors = require('cors');
const path = require('path');
const mongoose = require('mongoose');
const Message = require('/models/Message');  // Import the Mongoose model

const app = express();

// Use CORS middleware
app.use(cors({
    origin: '*',  // Allows all domains. You may change this to only allow certain domains if needed.
    methods: ['GET', 'POST', 'PUT', 'DELETE'],  // Allow specific HTTP methods.
    allowedHeaders: ['Content-Type'],  // Allow specific headers.
}));


// Parse JSON request bodies
app.use(express.json());

// Serve static files (adjust this based on your folder structure)
app.use(express.static(path.join(__dirname, '..', 'portfolio-responsive-complete')));

// MongoDB connection URI (use environment variable for Heroku)
const mongoURI = process.env.MONGO_URI || 'mongodb+srv://desiahbarnett:cora1951@cluster0.tsucj.mongodb.net/contact-form?retryWrites=true&w=majority';

// Connect to MongoDB
mongoose.connect(mongoURI)
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));

// Handle contact form submission (POST request)
app.post('/api/contact', async (req, res) => {
    const { name, email, message } = req.body;

    // Ensure all fields are provided
    if (!name || !email || !message) {
        return res.status(400).json({ error: 'All fields are required.' });
    }

    try {
        // Create a new Message instance and save to MongoDB
        const newMessage = new Message({ name, email, message });
        await newMessage.save();

        // Send a success response
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

// Start the server, listen on the port from environment variable (for Heroku) or fallback to 3000 (for local dev)
const port = process.env.PORT || 3000;  // Heroku assigns a port number dynamically
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);  // Log the port to the console
});
