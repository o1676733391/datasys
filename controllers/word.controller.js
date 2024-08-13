const word = require("../models/word.model");

const getwords = async (req, res) => {
  try {
    const words = await word.find({});
    res.status(200).json(words);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const getwordbyid = async (req, res) => {
  try {
    const { id } = req.params;

    const word_id = await word.findById(id);
    res.status(200).json(word_id);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const getword = async (req, res) => {
  try {
    const { wordfind } = req.params;

    const wordsearch = await word.findOne({ word: wordfind });

    if (!wordsearch) {
      return res.status(404).json({ message: "word not found" });
    }

    res.status(200).json(wordsearch);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const createword = async (req, res) => {
  try {
    const word_id = await word.create(req.body);

    res.status(200).json(word_id);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const updateword = async (req, res) => {
  try {
    const { id } = req.params;

    const word_update = await word.findByIdAndUpdate(id, {
      $set: req.body,
      $inc: { __v: 1 }, // Increment __v manually
    });

    if (!word_update) {
      return res.status(404).json({ message: "word not found" });
    }

    const updatedword = await word.findById(id);
    res.status(200).json(updatedword);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};


// WARNING: Dont test already 
const updateword_extra = async (req, res, word_new, type_word, path) => {
  try {
    const id = word_new.__id;
    word_new[type_word].img = path;
    const word = word_new;

    const word_update = await word.findByIdAndUpdate(id, {
      $set: word,
      $inc: { __v: 1 }, // Increment __v manually
    });

    if (!word_update) {
      return res.status(404).json({ message: "word not found" });
    }

    const updatedword = await word.findById(id);
    res.status(200).json(updatedword);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const deleteword = async (req, res) => {
  try {
    const { id } = req.params;

    const word_delete = await word.findByIdAndDelete(id);

    if (!word_delete) {
      return res.status(404).json({ message: "word not found" });
    }

    res.status(200).json({ message: "word deleted successfully" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

module.exports = {
  getwords,
  getwordbyid,
  getword,
  createword,
  updateword,
  updateword_extra,
  deleteword,
};
