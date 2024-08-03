const express = require("express");
const word = require("../models/word.model.js");

const router = express.Router();

const {getwords, getwordbyid, getword, createword, updateword, deleteword} = require('../controllers/word.controller.js');


router.get('/', getwords);
router.get("/:id", getwordbyid);

router.post("/", createword);

// update a product
router.put("/:id", updateword);

// delete a product
router.delete("/:id", deleteword);

router.get("/word/:wordfind", getword);

module.exports = router;
