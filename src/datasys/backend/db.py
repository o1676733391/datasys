from pymongo import MongoClient
import json

# Địa chỉ và cổng của MongoDB
mongo_uri = "mongodb://127.0.0.1:9191"  # Thay đổi nếu bạn có thông tin khác

def main():
    client = MongoClient(mongo_uri)

    try:
        # Kết nối đến MongoDB
        client.admin.command('ping')
        print("Kết nối thành công!")

        # Liệt kê tất cả các cơ sở dữ liệu
        databases = client.list_database_names()
        print("Danh sách cơ sở dữ liệu:")
        for db_name in databases:
            print(f" - {db_name}")

        # Database: Datasys
        db = client["Datasys"]
        print("Kết nối tới cơ sở dữ liệu Datasys thành công!")

        # Liệt kê tất cả các collection
        collections = db.list_collection_names()
        print("Danh sách các collection:")
        for col_name in collections:
            print(f" - {col_name}")

        # Connect to the collection "Dictionary"    
        dictionary = db["dictionary"]
        print("Kết nối tới collection Dictionary thành công!")

        # Fetch all documents in the collection "Dictionary"
        data = list(dictionary.find({}))
        count = dictionary.count_documents({})
        print(f"Số lượng documents trong collection Dictionary: {count}")
        # get all the words with "voice" field = "N/a"
        words = [d["word"] for d in data if d.get("voice") == "N/a"]
        print(f"Số lượng từ không có file âm thanh: {len(words)}")
        print("Danh sách các từ không có file âm thanh:")
        print(json.dumps(words, indent=4))
    except Exception as err:
        print(f"Kết nối thất bại: {err}")

if __name__ == "__main__":
    main()