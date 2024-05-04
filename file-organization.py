import os
import shutil

def organize_files(folder_path):
    # Define destination folders for different file types
    file_types = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Others': []  # Default folder for other file types
    }

    # Create destination folders if they don't exist
    for folder_name in file_types:
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Move files to their respective folders
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Get file extension
            file_ext = os.path.splitext(filename)[1].lower()
            # Find the appropriate folder for the file type
            destination_folder = 'Others'  # Default folder
            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    destination_folder = folder_name
                    break
            # Move the file to its destination folder
            src_file = os.path.join(folder_path, filename)
            dst_folder = os.path.join(folder_path, destination_folder)
            dst_file = os.path.join(dst_folder, filename)
            if not os.path.exists(dst_file):
                shutil.move(src_file, dst_folder)
                print(f"Moved '{filename}' to '{destination_folder}' folder.")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
