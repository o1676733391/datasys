const express = require("express");

const router = express.Router();

const { createvoice, getvoice } = require("../controllers/voice.controller.js");

router.post("/", createvoice);
router.get("/:filename", getvoice);

module.exports = router;
