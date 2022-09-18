import json
from typing import Any


def load_students() -> str:
    """
    Считывает студентов из файла
    :return:Возвращает данные о студентах
    """
    with open('students.json', 'rt', encoding='UTF-8') as file:
        students = json.load(file)
        return students


def load_professions() -> str:
    """
    Считывает профессии из файла
    :return: Возвращает данные о профессиях
    """
    with open('professions.json', 'rt', encoding='UTF-8') as file:
        professions = json.load(file)
        return professions


def get_student_by_pk(pk: Any, students: list[dict]):
    """
    :param pk:ID студента
    :param students: Студенты
    :return:Возвращает студента соответствующему данному ID
    """
    for i in range(len(students)):
        if students[i]['pk'] == pk:
            return students[i]


def get_profession_by_title(title: str, professions: Any) -> Any:
    """
    :param title: Название профессии
    :param professions: Файл с профессиями
    :return: Возвращает необходимые навыки для профессии
    """
    for i in range(len(professions)):
        if professions[i]['title'] == title:
            return professions[i]['skills']


def check_fitness(student: dict, profession: Any) -> dict:
    """
    :param student: Выбор студента
    :param profession: Выбор профессии
    :return: Возвращает проф пригодность в виде словаря
    """
    # Скиллы ученика
    skill_student = student['skills']
    # Скиллы профессии
    skill_profession = profession
    student_skills = set(skill_student)
    profession_skills = set(skill_profession)
    has = profession_skills.intersection(student_skills)
    lacks = profession_skills.difference(student_skills)
    fit_persent = len(has) / len(profession_skills) * 100
    available_knowledge = {
        "has": 'Необходимых знаний нет' if len(has) == 0 else has,
        "lacks": 'Нужные знания получены' if len(lacks) == 0 else lacks,
        "fit_percent": fit_persent
    }
    return available_knowledge
