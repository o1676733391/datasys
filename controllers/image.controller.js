const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { v4: uuidv4 } = require("uuid");
const { updateword_extra } = require("./word.controller");

// NOTE: setup upload storage include filename and location
const storageImage = multer.diskStorage({
  destination: function (req, file, cb) {
    const uploadDir = path.join(__dirname, "images");
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + "-" + uuidv4()); // format dateup-image id
  },
});

const uploadImage = multer({
  storage: storageImage,
  fileFilter: (req, file, cb) => {
    const allowedExtensions = /jpeg|jpg|png|gif/;
    const extname = allowedExtensions.test(
      path.extname(file.originalname).toLowerCase(),
    );
    if (extname) {
      cb(null, true);
    } else {
      cb(new Error("Invalid file type! Only images are allowed."));
    }
  },
}).single("image");

// Exception handler middleware
const exception_handler = (err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    res.status(500).json({ message: err.message });
  } else if (err) {
    res.status(500).json({ message: err.message });
  } else {
    next();
  }
};

// Create image function with error handling
const createimage = (req, res) => {
  try {
    // Call multer's upload function
    uploadImage(req, res, async function (err) {
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

      try {
        // NOTE: change value img in dtb
        const updateword = await updateword_extra( 
          req,
          res,
          req.body.word, // thong tin tu 
          req.body.type_word, // thong tin loai tu
          req.file.path, // buc anh
        );
      } catch (error) {
        res.status(500).json({
          message: "Ignore word infomation! | " + error,
        })
      }

      res.status(200).json({
        message: "Image uploaded successfully",
        filepath: req.file.path,
      });
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

const getimage = (req, res) => {
  const { filename } = req.params;
  const filepath = path.join(__dirname, "images", filename);

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
  createimage,
  getimage,
  exception_handler,
};
