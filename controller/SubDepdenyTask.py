import os

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

        # Print or use the log
        print("Deleted Files Log:", file_delete_log)