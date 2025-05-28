const express = require("express");
require("dotenv").config();
const sequelize = require("./models");

const app = express();
const port = process.env.PORT || 5000;

app.use(express.json());

app.get("/", (req, res) => {
  res.send("Backend is running and connected to DB");
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
