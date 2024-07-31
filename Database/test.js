const { MongoClient } = require("mongodb");

// Địa chỉ và cổng của MongoDB
const mongoUri = "mongodb://127.0.0.1:9191"; // Thay đổi nếu bạn có thông tin khác

async function testConnection() {
  const client = new MongoClient(mongoUri);

  try {
    // Kết nối đến MongoDB
    await client.connect();
    // Chọn cơ sở dữ liệu
    const db = client.db("local");
    // Chọn collection
    const collection = db.collection("startup_log");

    console.log("Kết nối thành công!");
    console.log(collection);
  } catch (err) {
    console.error(`Kết nối thất bại: ${err}`);
  } finally {
    // Đảm bảo đóng kết nối khi hoàn thành
    await client.close();
  }
}

// Gọi hàm để kiểm tra kết nối
testConnection();
