# -*- coding: utf-8 -*-
import argparse
import sys
import os

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YAMLDataReader import YAMLDataReader
from MyCalcRating import MyCalcRating


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    file_extension = os.path.splitext(path)[1]

    if file_extension == '.txt':
        reader = TextDataReader()
        students = reader.read(path)
        print("Students: ", students)

        rating = CalcRating(students).calc()
        print("Rating: ", rating)
    else:
        yamlReader = YAMLDataReader()
        yamlData = yamlReader.read(path)
        print("YAML: ", yamlData)

        excellent_students = MyCalcRating(yamlData).excellentStudents()
        print("Количество студентовотличников (имеющих баллы по всем "
              f"предметам ≥ 90) = {excellent_students}")


if __name__ == "__main__":
    main()
