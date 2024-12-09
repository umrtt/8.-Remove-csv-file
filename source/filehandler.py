from source.PathVerify import filePathValidation
from pathlib import Path

from dataclasses import dataclass



class fileHandle:
    def __init__(self, file_path, list_path):
        self.path: filePathValidation = filePathValidation(input_path = file_path,list_path = list_path)
    
    def _check_file(self):
        """Count occurrences of files that contain substrings from pred_list."""
        # Create a Path object for the main folder
        main_path = self.path.input_path
        
        # Initialize a dictionary to store counts for substrings in pred_list
        counts = {name: 0 for name in self.path.list_path}
        count_not_in_list = 0

        # Iterate through all files in the directory and subdirectories
        for file_path in main_path:
            if file_path.is_file():
                matched = False
                # Check if any substring from pred_list is in the file name
                for name in self.path.list_path:
                    if name in file_path.name:
                        counts[name] += 1
                        matched = True
                        break  # Stop checking after the first match
                
                if not matched:
                    count_not_in_list += 1

        # Add the count of files not in the list to the dictionary
        counts['remove_items'] = count_not_in_list
        self.__dict_print(counts)
        return counts
    
    @staticmethod
    def __dict_print(dic: dict):
        for key, value in dict.items():
            print(f'Found: {value} {key} ')


if __name__ == '__main__':
    setup_file = r'E:\2.WorkSpace\2.Python\8. Remove csv file\setup.txt'
    folder_path = r'E:\2.WorkSpace\2.Python\8. Remove csv file\test'
    