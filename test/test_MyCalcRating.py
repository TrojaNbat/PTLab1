from src.Types import DataType
from src.MyCalcRating import MyCalcRating, getScores
import pytest


class TestMyCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        excellent_students = 1
        data: DataType = {'Иванов Иван Иванович': [('математика', 67),
                                                   ('литература', 100),
                                                   ('программирование', 91)],
                          'Петров Петр Петрович': [('математика', 78),
                                                   ('химия', 87),
                                                   ('социология', 61)],
                          'Петров Николай Викторович': [('математика', 98),
                                                        ('химия', 97),
                                                        ('социология', 91)]}

        return data, excellent_students
