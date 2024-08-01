const word = require("../models/word.model");

const getwords = async (req, res) => {
  try {
    const words = await word.find({});
    res.status(200).json(words);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const getword = async (req, res) => {
  try {
    const { id } = req.params;
    const word_id = await word.findById(id);
    res.status(200).json(word_id);
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

    const word = await word.findByIdAndUpdate(id, req.body);

    if (!word) {
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

    const word = await word.findByIdAndDelete(id);

    if (!word) {
      return res.status(404).json({ message: "word not found" });
    }

    res.status(200).json({ message: "word deleted successfully" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

module.exports = {
  getwords,
  getword,
  createword,
  updateword,
  deleteword,
};
