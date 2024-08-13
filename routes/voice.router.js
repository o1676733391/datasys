const express = require("express");

const router = express.Router();

const { createvoice, getvoice } = require("../controllers/voice.controller.js");

router.post("/", createvoice);
router.get("/:fileid", getvoice);

module.exports = router;
