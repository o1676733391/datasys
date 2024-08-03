from pymongo import MongoClient
import gridfs

# Địa chỉ và cổng của MongoDB
mongo_uri = "mongodb://127.0.0.1:9191"  # Thay đổi nếu bạn có thông tin khác

def upload_file(file_path, file_id):
    client = MongoClient(mongo_uri)
    db = client["Datasys"]
    fs = gridfs.GridFS(db)

    try:
        # Open the file in read-binary mode
        with open(file_path, 'rb') as f:
            # Upload the file to GridFS with the specified _id
            fs.put(f, _id=file_id, filename=file_path)
        print(f"File {file_path} uploaded successfully with _id {file_id}!")
    except Exception as err:
        print(f"Failed to upload file: {err}")

if __name__ == "__main__":
    file_path = "datasys/data/sound/66aa36aa2576d8d338632950.mp3"
    file_id = "66aa36aa2576d8d338632950"
    upload_file(file_path, file_id)