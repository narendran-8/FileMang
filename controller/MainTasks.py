import sys
import os
import subprocess

#User modules
from controller import SubDepdenyTask 

class AllTask:
    def __init__(self):
        print("\n📂 File Management CLI")
        print("1️⃣ Cleanup all files in a directory")
        print("2️⃣ Compress files in a directory")
        print("3️⃣ Exit")
        self.STask = SubDepdenyTask.SubTask()

    def cleanup_menu(self):
        directory = input("📁 Enter the directory path: ").strip()
        if not os.path.isdir(directory):
            print("❌ Invalid directory!")
            return
        # Import function from 
        self.STask.delete_all_files(directory)

    def compress_menu(self):
        directory = input("📁 Enter the directory path: ").strip()
        compressed_file_name = input("📦 Enter compressed file name: ").strip()
        single_file = input("📄 Enter file to compress (or leave blank for all files): ").strip()
        format = input("🔄 Compression format (zip/tar): ").strip().lower()
        delete_original = input("❌ Delete original files after compression? (yes/no): ").strip().lower() == 'yes'
        
        compress_files(directory, compressed_file_name, single_file if single_file else None, format, delete_original)
