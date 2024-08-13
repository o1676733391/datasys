const mongoose = require("mongoose");

const VoiceSchema = mongoose.Schema(
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
const Voice = mongoose.model("voice", VoiceSchema, "fs.files");

module.exports = Voice;
