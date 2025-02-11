from pymongo import MongoClient

# MongoDB connection (Docker container)
client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["file_logs"]  # Database name
collection = db["deleted_files"]  # Collection name