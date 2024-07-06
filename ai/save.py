import os
import shutil

def save_file(file):
    upload_directory = "../ai/uploads"
    os.makedirs(upload_directory, exist_ok=True)  # Create the directory if it doesn't exist
    file_path = os.path.join(upload_directory, file.filename)

    # Save the uploaded file
    file_obj = open(file_path, "wb")
    shutil.copyfileobj(file.file, file_obj)


save_file()