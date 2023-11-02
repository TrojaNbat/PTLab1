from DataReader import DataReader
from Types import DataType
import yaml


class YAMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.Loader)
            for student in data:
                itemNumber, items = list(student.items())[0]
                self.students[itemNumber] = []
                for item in items.keys():
                    score = items.get(item)
                    self.students[itemNumber].append((item, score))

        return self.students
