const express = require("express");

const router = express.Router();

const { createimage, getimage } = require("../controllers/image.controller.js");

router.post("/", createimage);
router.get("/:filename", getimage);

module.exports = router;
