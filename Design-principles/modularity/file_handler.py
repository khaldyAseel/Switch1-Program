import os

class FileHandler:
    @staticmethod
    def write_file(filepath, content):
        with open(filepath, 'w') as file:
            file.write(content)

    @staticmethod
    def read_file(filepath):
        with open(filepath, 'r') as file:
            return file.read()

    @staticmethod
    def file_exists(filepath):
        return os.path.exists(filepath)

    @staticmethod
    def delete_file(filepath):
        if os.path.exists(filepath):
            os.remove(filepath)
