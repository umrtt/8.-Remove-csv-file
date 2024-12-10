from .PathVerify import filePathValidation
from pathlib import Path




class fileHandle:
    def __init__(self, file_path, list_path) -> None:
        self.path: filePathValidation = filePathValidation(input_path = file_path,list_path = list_path)
    
    def check_file(self) -> dict:
        """Count occurrences of files that contain substrings from pred_list."""
        # Initialize a dictionary to store counts for substrings in pred_list
        counts = {name: 0 for name in self.path.list_path}
        count_not_in_list = 0
        
        # Iterate through all files in the directory and subdirectories
        for file_path in self.path.input_path.rglob('*.csv'):
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
    def remove_csv_file(self) -> None:
        for file in self.path.input_path.rglob('*csv'):
            if not self.__should_ignore(file,self.path.list_path):
                print(f'Remove: {file.name}')
                file.unlink()
    def keeping_items_show(self):
        keeping_list = ','.join(self.path.list_path)
        print(f"Keeping item: {keeping_list}")
    @staticmethod
    def __dict_print(dic: dict) -> None:
        for key, value in dic.items():
            print(f'Found: {value} {key} ')

    # check whether we need to remove file or not
    @staticmethod
    def __should_ignore(file_name:Path, ignore_words:list) -> bool:
        return any(word in file_name.name for word in ignore_words)

