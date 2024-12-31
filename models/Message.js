const mongoose = require('mongoose');

// Define the schema for contact form submissions
const messageSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    message: { type: String, required: true },
    date: { type: Date, default: Date.now }
});

// Create the model using the schema
const Message = mongoose.model('Message', messageSchema);

module.exports = Message;
