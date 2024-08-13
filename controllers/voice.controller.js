const { GridFSBucket, ObjectId } = require("mongodb");
const mongoose = require("mongoose");

const getvoice = async (req, res) => {
  const { fileid } = req.params;

  try {
    // FIX: rat ngu hoc aka stupid, fk u nodejs fk u mongodb too
    // fk everything  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 
    // day la cam xuc ca nhan xin thong cam
    
    // NOTE: its work! 
    // https://www.mongodb.com/docs/drivers/node/current/fundamentals/gridfs/
    // read above docs and feel
    const bucket = new GridFSBucket(mongoose.connection.db, {
      bucketName: "fs", 
    });

    const cursor = bucket.find({});
    bucket
      .openDownloadStream(new ObjectId(fileid))
      .pipe(res);
    
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).json({ message: error.message });
  }
};

module.exports = {
  createvoice,
  getvoice,
};
