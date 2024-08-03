const express = require("express");
const mongoose = require("mongoose");
const Product = require("./models/word.model.js");
const productRoute = require("./routes/word.route.js");
const app = express();

// middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// routes
// app.use("/api/products", productRoute);
app.use("/", productRoute);

// app.get("/", (req, res) => {
//   res.send("Hello from Node API Server Updated");
// });

mongoose
  .connect(
    process.env.DATABASE_URL,
  )
  .then(() => {
    console.log("connected to database!");
    app.listen(3000, () => {
      console.log("server is running on port 3000");
      console.log("http://localhost:3000");
    });
  })
  .catch(() => {
    console.log("connection failed!");
  });
