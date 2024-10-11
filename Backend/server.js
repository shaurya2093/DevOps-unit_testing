const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');
const cors = require('cors');

const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname));

const PORT = process.env.PORT || 8081;

// Connect to MongoDB (ensure to use your actual MongoDB URI)
const MONGODB_URI = 'mongodb+srv://guptashaurya507:shaurya@contact.3ioln.mongodb.net/';
mongoose.connect(MONGODB_URI)
    .then(() => {
        console.log('Connected to MongoDB');
        // Start the server only after successful connection
        app.listen(PORT, () => {
            console.log(`Server is running on port ${PORT}`);
        });
    })
    .catch(error => {
        console.error('MongoDB connection failed:', error);
    });

// Define the Contact Schema
const contactSchema = new mongoose.Schema({
    name: String,
    email: String,
    subject: String,
    message: String
});

// Create a model for Contact
const Contact = mongoose.model('Contact', contactSchema);
app.get('/contact2', (req, res) => {
    res.send('This is the contact page');
});
// Handle the form submission
app.post('/contact', async (req, res) => {
    const { name, email, subject, message } = req.body;

    const newContact = new Contact({
        name: name,
        email: email,
        subject: subject,
        message: message
    });

    try {
        await newContact.save();
        res.send('Thank you for your message! We will get back to you soon.');
    } catch (error) {
        console.error(error);
        res.status(500).send('There was an error submitting your message.');
    }
});
