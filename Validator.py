import re
from tqdm import tqdm

class validator:
    """Validator class to get count_valid_records / count_invalid_records / count_invalid_arguments"""
    value: list

    def __init__(self, array) -> None:
        """Constructor: gets copy them to local list"""
        self.value = array.copy()

    def validation(self, index) -> dict:
        """Function: Get valid / invalid writes"""

        rezult = {"email": self.check_email(index),
                  "height": self.check_height(index),
                  "snils": self.check_snils(index),
                  "passport_number": self.check_passport_number(index),
                  "university": self.check_university(index),
                  "age": self.check_age(index),
                  "academic_degree": self.check_academic_degree(index),
                  "worldview": self.check_worldview(index),
                  "address": self.check_address(index)}
        return rezult.copy()

    def count_valid_records(self) -> int:
        """Function: Get count valid writes"""

        count_correct = 0
        for i in tqdm(range(len(self.value)), desc="Подсчёт корректных записей"):
            if not (False in self.validation(i).values()):
                count_correct += 1
        return count_correct

    def count_invalid_records(self) -> int:
        """Function: Get count invalid writes"""

        count_incorrect = 0
        for i in tqdm(range(len(self.value)), desc="Подсчёт некорректных записей"):
            if False in self.validation(i).values():
                count_incorrect += 1
        return count_incorrect

    def count_invalid_arguments(self) -> list:
        """Function: Get valid writes"""

        count_inv = [0] * 9
        for i in tqdm(range(len(self.value)),
                      desc="Подсчёт некорректных записей  данных"):
            if not self.check_email(i):
                count_inv[0] += 1
            if not self.check_height(i):
                count_inv[1] += 1
            if not self.check_snils(i):
                count_inv[2] += 1
            if not self.check_passport_number(i):
                count_inv[3] += 1
            if not self.check_university(i):
                count_inv[4] += 1
            if not self.check_age(i):
                count_inv[5] += 1
            if not self.check_academic_degree(i):
                count_inv[6] += 1
            if not self.check_worldview(i):
                count_inv[7] += 1
            if not self.check_address(i):
                count_inv[8] += 1
        return count_inv

    def check_email(self, num) -> bool:
        """Function: check telephone"""

        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.value[num]["email"]):
            return True
        return False

    def check_height(self, num) -> bool:
        """Function: check height"""
        try:
            float_height = float(self.value[num]["height"])
            return 2.2 > float_height > 1.2
        except ValueError:
            return False

    def check_snils(self, num) -> bool:
        """Function: check snils"""

        pattern = r'[0-9]{11}$'
        if re.match(pattern, self.value[num]["snils"]):
            return True
        return False

    def check_passport_number(self, num) -> bool:
        """Function: check passport number"""

        if isinstance(self.value[num]["passport_number"], int):
            if 100000 <= self.value[num]["passport_number"] < 1000000:
                return True
        return False

    def check_university(self, num) -> bool:
        """Function: check occupation"""

        pattern = "^.*([У|у]нивер|[А|а]кадем|[T|т]ех|[И|и]нститут|им\.|[И-и]сслед|[А-Я]{2,}).*$"
        if re.match(pattern, self.value[num]["university"]):
            return True
        return False

    def check_age(self, num) -> bool:
        """Function: check age"""

        if isinstance(self.value[num]["age"], int):
            if 14 <= self.value[num]["age"] < 100:
                return True
        return False

    def check_academic_degree(self, num) -> bool:
        """Function: check academic degree"""

        pattern = "[a-zA-Zа-яА-Я]+"
        if re.match(pattern, self.value[num]["academic_degree"]):
            return True
        return False

    def check_worldview(self, num) -> bool:
        """Function: check worldview"""

        pattern = "[a-zA-Zа-яА-Я]+"
        if re.match(pattern, self.value[num]["worldview"]):
            return True
        return False

    def check_address(self, num) -> bool:
        """Function: check address"""

        pattern = ".+[0-9]+"
        if re.match(pattern, self.value[num]["address"]):
            return True
        return False

