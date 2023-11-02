# -*- coding: utf-8 -*-
from Types import DataType


def getScores(student) -> list:
    items = student[1]
    scores = [score for score in items if score[1] >= 90]
    print(scores)
    return scores


class MyCalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def excellentStudents(self) -> int:
        excellent_students = 0
        for student in self.data.items():
            scores = getScores(student)
            if len(scores) == len(student) + 1:
                excellent_students += 1

        return excellent_students
