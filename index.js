const { exception_handler } = require("./controllers/image.controller.js");
const express = require("express");
const mongoose = require("mongoose");
const Product = require("./models/word.model.js");

const productRoute = require("./routes/word.route.js");
const imageRoute = require("./routes/image.router.js");
const voiceRoute = require("./routes/voice.router.js");
const app = express();

// middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(exception_handler); // middleware for cath err while uploading files

// routes
// app.use("/api/products", productRoute);
app.use("/", productRoute);
app.use("/image", imageRoute);
app.use("/voice", voiceRoute);

mongoose
  .connect(process.env.DATABASE_URL)
  .then(() => {
    console.log("Connected to database!");
    app.listen(3000, () => {
      console.log("Server is running on port 3000");
      console.log("http://localhost:3000");
    });
  })
  .catch((err) => {
    console.error("Connection failed!", err);
  });

