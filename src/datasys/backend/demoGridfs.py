from pymongo import MongoClient
import gridfs

# Địa chỉ và cổng của MongoDB
mongo_uri = "mongodb://127.0.0.1:9191"  # Thay đổi nếu bạn có thông tin khác

def retrieve_file_from_gridfs_by_word(word):
    client = MongoClient(mongo_uri)
    db = client["Datasys"]
    fs = gridfs.GridFS(db)
    dictionary_collection = db["dictionary"]

    try:
        # Retrieve the document from the "dictionary" collection using the provided word
        document = dictionary_collection.find_one({"word": word})
        if document and "voice" in document:
            voice_id = document["voice"]

            # Find the file in GridFS using the _id
            file_data = fs.find_one({"_id": voice_id})
            if file_data:
                output_path = "retrieved_file.mp3"
                # Write the file data to the specified output path
                with open(output_path, 'wb') as f:
                    f.write(file_data.read())
                print(f"File with _id {voice_id} retrieved successfully and saved to {output_path}!")
            else:
                print(f"No file found in GridFS with _id {voice_id}.")
        else:
            print(f"No document found in the 'dictionary' collection with word '{word}' or 'voice' field not present.")
    except Exception as err:
        print(f"Failed to retrieve file: {err}")



if __name__ == "__main__":
    # Example usage
    example_word = "thực hiện"  # Replace with the actual word you want to use
    retrieve_file_from_gridfs_by_word(example_word)