const express = require("express");
const word = require("../models/word.model.js");

const router = express.Router();

const {getwords, getword, createword, updateword, deleteword} = require('../controllers/word.controller.js');


router.get('/', getwords);
router.get("/:id", getword);

router.post("/", createword);

// update a product
router.put("/:id", updateword);

// delete a product
router.delete("/:id", deleteword);




module.exports = router;
