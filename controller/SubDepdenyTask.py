import os
from controller import dbmanage

class SubTask:
    def __init__(self):
        pass

    def delete_all_files(self, directory):
        """Deletes all files in a specified directory"""
        if not os.path.isdir(directory):
            print(f"❌ Error: {directory} is not a valid directory.")
            return
        file_delete_log = []  # Use a list to store multiple file entries

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                try:
                    file_size = os.path.getsize(filepath) / (1024 * 1024)  # Convert bytes to MB
                    os.remove(filepath)
                    file_delete_log.append({
                        "filename": filename,
                        "filepath": filepath,
                        "file_size": file_size
                    })
                    print(f"✅ Deleted: {filepath}")
                except Exception as e:
                    print(f"❌ Error deleting {filepath}: {e}")

        # Save the log to MongoDB
        if file_delete_log:
            dbmanage.collection.insert_many(file_delete_log)
            print("✅ Logs saved to MongoDB.")
        else:
            print("⚠️ No files were deleted.")

        # Print the log for reference
        # print("Deleted Files Log:", file_delete_log)
