import json
from tqdm import tqdm
from Validator import validator

class write_file:
    """Write file data by path name"""

    def __init__(self, file_path) -> None:
        """Contstructor: writes path"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Function: reads data from file"""

        tmp = []
        for i in tqdm(range(len(array.value)), desc="Запись результата валидации в файл"):
            if not (False in array.validation(i).values()):
                tmp.append(array.value[i].copy())
        json.dump(tmp, open(self.path,"w",encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

