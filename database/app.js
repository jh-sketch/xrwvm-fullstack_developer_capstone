const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3030;

app.use(cors());
app.use(require('body-parser').urlencoded({ extended: false }));

const reviews_data = JSON.parse(fs.readFileSync("reviews.json", 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync("dealerships.json", 'utf8'));

mongoose.connect("mongodb://mongo_db:27017/", { dbName: 'dealershipsDB' });

const Reviews = require('./review');
const Dealerships = require('./dealership');

try {
  Reviews.deleteMany({}).then(() => {
    Reviews.insertMany(reviews_data['reviews']);
  });
  Dealerships.deleteMany({}).then(() => {
    Dealerships.insertMany(dealerships_data['dealerships']);
  });
} catch (error) {
  console.error("Error seeding database:", error);
}

// Home route
app.get('/', async (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Fetch reviews by dealer id
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({ dealership: parseInt(req.params.id) });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    const dealers = await Dealerships.find();
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships' });
  }
});

// Fetch dealerships by state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const state = req.params.state.toUpperCase();
    const dealers = await Dealerships.find({ state: state });
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealers by state' });
  }
});

// Fetch dealer by id
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const dealer = await Dealerships.findOne({ id: parseInt(req.params.id) });
    if (!dealer) {
      return res.status(404).json({ error: 'Dealer not found' });
    }
    res.json(dealer);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealer by id' });
  }
});

// List all distinct states (top-level)
app.get('/listStates', async (req, res) => {
  try {
    const states = await Dealerships.distinct('state');
    res.json(states);
  } catch (error) {
    res.status(500).json({ error: 'Error listing states' });
  }
});

// List all distinct states under /fetchDealers/listStates
app.get('/fetchDealers/listStates', async (req, res) => {
  try {
    const states = await Dealerships.distinct('state');
    res.json(states);
  } catch (error) {
    res.status(500).json({ error: 'Error listing states' });
  }
});

// Insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  let data;
  try {
    data = JSON.parse(req.body);
  } catch {
    return res.status(400).json({ error: 'Invalid JSON in request body' });
  }

  try {
    const documents = await Reviews.find().sort({ id: -1 });
    const new_id = documents.length ? documents[0].id + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});