
from typing import List

class Teaching:
    def __init__(self, id: int, surname: str, name: str, patronymic: str):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    @classmethod
    def get_by_id(cls, teaching_id):
        teachers_data = {
            1: {"surname": "Иванов", "name": "Иван", "patronymic": "Иванович"}
        }

        if teaching_id in teachers_data:
            data = teachers_data[teaching_id]
            return cls(id=teaching_id, surname=data["surname"], name=data["name"], patronymic=data["patronymic"])
        else:
            return None


class Student:
    def __init__(self, id: int, surname: str, name: str, patronymic: str):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"
    
    @classmethod
    def get_by_id(cls, student_id):
        students_data = {
            1: {"surname": "Петров", "name": "Дима", "patronymic": "Петрович"},
            2: {"surname": "Сидоров", "name": "Петр", "patronymic": "Степанович"},
            3: {"surname": "Максимов", "name": "Николай", "patronymic": "Михайлович"},
            4: {"surname": "Петухов", "name": "Павел", "patronymic": "Петрович"},
        }

        if student_id in students_data:
            data = students_data[student_id]
            return cls(id=student_id, surname=data["surname"], name=data["name"], patronymic=data["patronymic"])
        else:
            return None

class StudyGroup:
    def __init__(self, teaching: Teaching, students: List[Student]):
        self.teaching = teaching
        self.students = students

    def __str__(self):
        teaching_info = str(self.teaching)
        students_info = ', '.join([str(student) for student in self.students])
        return f"Учебная группа\nПреподаватель: {teaching_info}\nСтуденты: {students_info}"
    
    
class StudyGroupServis:
    @staticmethod
    def form_group(teaching: Teaching, students: List[Student]) -> StudyGroup:
        return StudyGroup(teaching, students)

class StudyController:
    @staticmethod
    def create_study_group(teaching_id: int, student_ids: List[int]) -> StudyGroup:
        teaching = Teaching.get_by_id(teaching_id)
        students = [Student.get_by_id(student_id) for student_id in student_ids]
        study_group = StudyGroupServis.form_group(teaching, students)
        return study_group

# пример
teaching_id = 1
student_ids = [1, 2, 3, 4]

study_group = StudyController.create_study_group(teaching_id, student_ids)

print(study_group)


