const mongoose = require("mongoose");


// NOTE: common properties of categories 
const properties_category = {
  desc: {
    type: String,
  },

  example: {
    type: String,
  },

  synonym: {
    type: String,
  },

  antonym: {
    type: String,
  },

  img: {
    type: String,
  },
};

const WordSchema = mongoose.Schema({
  word: {
    type: String,
    required: [true, "Please enter product name"],
  },

  voice: {
    type: String,
  },

  status: {
    type: String,
    enum: [-1, 0, 1],
    required: [true, "Status must have one of -1 or 1 or 0"],
  },
  
  verb: properties_category,
  noun: properties_category,
  adj: properties_category,
});

// NOTE: call name collection dictionary
const Word = mongoose.model("dictionary", WordSchema, 'dictionary');

module.exports = Word;
