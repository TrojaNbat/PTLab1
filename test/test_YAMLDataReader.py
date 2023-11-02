# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


class TestYAMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        path = "data/data.yaml"

        data = {'Иванов Иван Иванович': [('математика', 67),
                                         ('литература', 100),
                                         ('программирование', 91)],
                'Петров Петр Петрович': [('математика', 78),
                                         ('химия', 87),
                                         ('социология', 61)],
                'Петров Николай Викторович': [('математика', 98),
                                         ('химия', 97),
                                         ('социология', 91)]}

        return path, data

    def test_read(self, file_and_data_content: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(file_and_data_content[0])
        assert file_content == file_and_data_content[1]
