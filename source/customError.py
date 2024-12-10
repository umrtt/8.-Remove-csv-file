class BaseException(Exception):
    def __init__(self,type, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.type= type
        self.message = message
        # Now for your custom code...
    def __str__(self):
        return f'[{self.type}]: {self.message}'
    
class NoImageExist(BaseException):
    pass

class setupFormatIncorrect(BaseException):
    pass

class FilePathNoExist(BaseException):
    pass

class ModelExtentionInvalid(BaseException):
    pass