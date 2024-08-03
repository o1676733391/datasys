from pymongo import MongoClient
import gridfs

# Địa chỉ và cổng của MongoDB
mongo_uri = "mongodb://127.0.0.1:9191"  # Thay đổi nếu bạn có thông tin khác

def retrieve_file(file_id, output_path):
    client = MongoClient(mongo_uri)
    db = client["Datasys"]
    fs = gridfs.GridFS(db)

    try:
        # Retrieve the file from GridFS using the specified _id
        file_data = fs.get(file_id)
        
        # Write the file data to the specified output path
        with open(output_path, 'wb') as f:
            f.write(file_data.read())
        print(f"File with _id {file_id} retrieved successfully and saved to {output_path}!")
    except Exception as err:
        print(f"Failed to retrieve file: {err}")

if __name__ == "__main__":
    file_id = "66aa36aa2576d8d338632950"
    output_path = "retrieved_file.mp3"
    retrieve_file(file_id, output_path)