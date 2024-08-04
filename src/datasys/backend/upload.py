from pymongo import MongoClient
import gridfs
import os

# Địa chỉ và cổng của MongoDB
mongo_uri = "mongodb://127.0.0.1:9191"  # Thay đổi nếu bạn có thông tin khác

def retrieve_and_upload_files():
    client = MongoClient(mongo_uri)
    db = client["Datasys"]
    dictionary_collection = db["dictionary"]
    fs = gridfs.GridFS(db)

    try:
        # Retrieve all documents from the "dictionary" collection
        documents = dictionary_collection.find({}, {"_id": 1})
        ids = [doc["_id"] for doc in documents]

        if ids:
            for _id in ids:
                file_path = f"datasys/data/sound/{_id}.mp3"
                
                # Check if the file exists
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as file_data:
                        # Upload file to GridFS
                        file_id = fs.put(file_data, filename=f"{_id}.mp3")
                        
                        # Update the "voice" field in the "dictionary" collection
                        dictionary_collection.update_one(
                            {"_id": _id},
                            {"$set": {"voice": file_id}}
                        )
                        print(f"Successfully uploaded {_id}.mp3 to GridFS and updated 'voice' field.")
                else:
                    print(f"File {file_path} does not exist.")
        else:
            print("No documents found in the 'dictionary' collection.")
    except Exception as err:
        print(f"Failed to retrieve and upload files: {err}")

# Call the function
retrieve_and_upload_files()