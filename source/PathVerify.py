from pathlib import Path
from pydantic import ( # type: ignore
    BaseModel,  
    field_validator,
    Field)

from .customError import *

from typing import List

def _read_file(file_path:Path):
    with open(file_path) as f:
        file = [line.strip() for line in f.readlines()]
    return file

class filePathValidation(BaseModel):
    """Verify the input path input:
    1. Check whether there is image contain in inputpath
    2. Checking the input_path and model_path is exist.
    3. Checking the model input file extention
    4. Check and creat the output of NG and OK image if it does not exist"""
    input_path: str = Field('Input path for remove image')
    list_path: str = Field('Setup file path')
    #verify input path
    @field_validator("input_path")
    @classmethod
    def is_contain_csv(cls, path:str) -> List:
        folder = Path(path)
        if not folder.is_dir():
            raise FilePathNoExist('FolderNoExist',"Folder khong ton tai")
        csv_files = folder.rglob('*.csv')
        print(f'Tim thay: {len(list(csv_files))} csv files')
        return folder
    #verify output path
    @field_validator("list_path")
    @classmethod
    def is_setup_file(cls,path:str) -> List:
        folder = Path(path)
        if not folder.is_file():
            raise FilePathNoExist('FileNoExist',"File setup khong ton tai")
        if folder.suffix.lower() != '.txt':
            raise setupFormatIncorrect('FileInvalid','Setup file phai co dang .txt')
        # Create subfolders if they do not exist
        return _read_file(folder)
    

