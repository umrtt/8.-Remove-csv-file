import PySimpleGUI as sg
from source.filehandler import fileHandle

class RemoveCsvFileApp:
    sg.theme('Default1')
    def __init__(self):
        # Define the layout
        self._outputBox = sg.Output(size=(65, 20), key='-OUTPUT-')
        self.layout = [
            [sg.Text('Folder Path', size=(10, 1)), sg.InputText(key='-INPUT_PATH-'), sg.FolderBrowse()],
            [sg.Text('Setup Path', size=(10, 1)), sg.InputText(key='-SETUP_PATH-',default_text='setup.txt'), sg.FileBrowse()],
            [sg.Button('Check'),sg.Button('Show'),sg.Button('Remove'), sg.Button('Clear Output'), sg.Button('Exit')],
            [self._outputBox]
        ]
        self.__is_loaded = False
        # Create the window with a gray background
        self.window = sg.Window('CSV File Remove', self.layout, finalize=True,icon='icon.ico')

    def run(self):
        # Event loop
        while True:
            event, values = self.window.read()
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            try:
                if event == 'Check':
                    self.check_file(values)
                if event == 'Show':
                    self.show_items(values)
                if event == 'Remove':
                    self.remove_items(values)
                if event == 'Clear Output':
                    self.clear_output()
            except Exception as e:
                print(e)

        self.window.close()
    def remove_items(self,values):
        self.__is_class_loaded(values=values)
        self.file_handle.remove_csv_file()
    def show_items(self,values):
        self.__is_class_loaded(values=values)
        self.file_handle.keeping_items_show()

    def check_file(self,values):
        self.__is_class_loaded(values=values)
        self.file_handle.check_file()

    def clear_output(self):
        # Clear the output area
        self.window['-OUTPUT-'].update('')
    def __is_class_loaded(self,values):
        if not values['-INPUT_PATH-']:
            raise FileExistsError('Vui long chon thu muc can xoa')
        if not self.__is_loaded:
            self.file_handle = fileHandle(file_path=values['-INPUT_PATH-'],
                                          list_path=values['-SETUP_PATH-'])
            self.__is_loaded = True

if __name__ == '__main__':
    app = RemoveCsvFileApp()
    app.run()