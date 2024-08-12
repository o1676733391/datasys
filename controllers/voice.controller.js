const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { v4: uuidv4 } = require("uuid");

const storageVoice = multer.diskStorage({
  destination: function (req, file, cb) {
    const uploadDir = path.join(__dirname, "voices");
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + "-" + uuidv4()); // format dateup-image id
  },
});

const uploadVoice = multer({
  storage: storageVoice,
  fileFilter: (req, file, cb) => {
    const allowedExtensions = /mp4|mp3/;
    const extname = allowedExtensions.test(
      path.extname(file.originalname).toLowerCase(),
    );
    if (extname) {
      cb(null, true);
    } else {
      cb(new Error("Invalid file type! Only images are allowed."));
    }
  },
}).single("voice");

// Create image function with error handling
const createvoice = (req, res) => {
  console.log(req);
  try {
    // Call multer's upload function
    uploadVoice(req, res, async function (err) {
      if (err) {
        // If multer throws an error, handle it here
        return res.status(500).json({ message: err.message });
      }

      // If no file is provided
      if (!req.file) {
        return res
          .status(400)
          .json({ message: "No file uploaded or file type not allowed" });
      }

      const updateword = await updateword_extra(
        req,
        res,
        req.body.word,
        req.body.type_word,
        req.file.path,
      );

      // Success, return the file path
      res.status(200).json({
        message: "Voice uploaded successfully",
        filepath: req.file.path,
      });
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const getvoice = (req, res) => {
  const { filename } = req.params;
  const filepath = path.join(__dirname, "voices", filename);

  // Check if the file exists
  fs.access(filepath, fs.constants.F_OK, (err) => {
    if (err) {
      // If the file doesn't exist, send a 404 response
      return res.status(404).json({ message: "Image not found" });
    }

    // If the file exists, send it as a response
    res.sendFile(filepath, (err) => {
      if (err) {
        res.status(500).json({ message: "Error sending the file" });
      }
    });
  });
};

module.exports = {
  createvoice,
  getvoice,
};
