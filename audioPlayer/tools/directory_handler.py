
import os

class DirectoryHandler():
    
    def __init__(self):
        self.base_directory = "."
        self.current_directory = "."
        self.selected_file = None
        pass
    
    def set_base_directory(self, base_directory):
        self.base_directory = base_directory
    
    def get_base_directory(self):
        return self.base_directory

    def set_current_directory(self, current_directory):
        self.current_directory = current_directory

    def get_current_directory(self):
        return self.current_directory

    def list_directory_contents(self):
        with os.scandir(self.current_directory) as entries:
            return [(entry.name, entry.is_dir()) for entry in entries]
    
    def set_selected_file(self, selected_file):
        self.selected_file = selected_file

    def get_selected_file(self):
        return self.selected_file
