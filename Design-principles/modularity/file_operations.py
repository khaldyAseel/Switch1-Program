# Acoording to the design principles Modularity
# we will devide the code into moduls

import os
from file_handler import FileHandler

class StorageManager:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def handle_file(self, filename, content):
        filepath = os.path.join(self.directory, filename)

        # File operations
        FileHandler.write_file(filepath, content)
        data = FileHandler.read_file(filepath)
        print(f"Loaded {filename.split('.')[0]}: {data}")

        # Check file existence
        if FileHandler.file_exists(filepath):
            print(f"File '{filepath}' exists.")
        else:
            print(f"File '{filepath}' does not exist.")

        # Delete file
        FileHandler.delete_file(filepath)
        print(f"Data deleted for {filename}.")

        # Verify deletion
        if not FileHandler.file_exists(filepath):
            print(f"Key '{filename.split('.')[0]}' successfully deleted.")


def main():
    directory = "data_storage"
    manager = StorageManager(directory)

    manager.handle_file("username.txt", "JohnDoe")
    manager.handle_file("email.txt", "john.doe@example.com")

if __name__ == "__main__":
    main()


