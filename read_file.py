import json

class read_file:
    """Reads file data by path name"""

    def __init__(self, file_path) -> None:
        """Contstructor: writes path"""
        self.path = file_path

    def read_file(self) -> list:
        """Function: writes data to class self"""

        array: list = []
        data = json.load(open(self.path, encoding="windows-1251"))
        for i in data:
            array.append(dict(i.copy()))
        return array