
const mongoose = require("mongoose");

const ChunkSchema = mongoose.Schema(
  {
    filename: String,
    chunkSize: Number,
    length: Number,
    uploadDate: Date
  },
  {
    optimisticConcurrency: true,
  },
);

// NOTE: call name collection dictionary

const Chunk = mongoose.model("chunk", ChunkSchema, "fs.chunks");

module.exports = Chunk;
