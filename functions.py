import json


def load_students(file_name):
    """
    Функция открывает файл с студентами и конвертирует ее
    из JSON в формат Python
    """
    with open(file_name, "r", encoding="utf-8") as file:
        students = json.load(file)
        return students


def load_professions(file_name):
    """
    Функция открывает файл с профессиями и конвертирует ее
    из JSON в формат Python
    """
    with open(file_name, "r", encoding="utf-8") as file:
        professions = json.load(file)
        return professions


def get_student_by_pk(pk):
    """
    Функция проверяет есть ли студент с таким порядковым номером
    и возвращает всю информацию про этого студента,
    если он есть.
    """
    students = load_students("students.json")
    for student in students:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title):
    """
    Функция проверяет есть ли профессия с таким названием
    и возвращает всю информацию про эту профессию,
    если она есть.
    """
    professions = load_professions("professions.json")
    for profession in professions:
        if profession["title"].lower() == title.lower():
            return profession


def check_fitness(student, profession):
    """
    Получает изученные языки для профессии
    недостающие языки программирования для профессии
    высчитывает насколько подходит студент для профессии
    """
    result = {}

    # Получаем изученные студентом языки программирования
    student_skill = set(student["skills"])
    # Получаем необходимые языки программирования для данной профессии
    skill_list = set(profession["skills"])
    # Получаем изученные языки программирования для данной профессии
    has = student_skill.intersection(skill_list)
    # Получаем недостоющие языки программирования языки программирования для данной профессии
    lacks = skill_list.symmetric_difference(has)
    # Вычисляем процент насколько подходит данный студент для данной профессии
    fit_percent = int(100 / len(skill_list)) * len(has)

    # Добавляем в словарь с результатом вычисления
    result["has"] = has
    result["lacks"] = lacks
    result["fit_percent"] = fit_percent

    # Вовзращает словарь с результатом вычислений
    return result


def main():
    """
    Основной код программы
    """
    width = 60
    fillchar = ' '

    # Получаем номер студента
    user_input_student = int(input("Введите номер студента: ".rjust(width, fillchar)))

    # Проверяем есть ли такой студент, если есть возвращаем информацию про него
    student = get_student_by_pk(user_input_student)

    # Если студент найден выводим информацию про него
    if student is not None:
        print(f"Студент {student['full_name']}.")
        print(f"Знает {', '.join(student['skills'])}.")

        # Проверяем есть ли профессия для проверки
        user_input_profession = input(f"Выберите специальность для оценки"
                                      f" студента {student['full_name']}.".rjust(width, fillchar))
        profession = get_profession_by_title(user_input_profession)

        # Если профессия найдена
        if profession is not None:
            check_fitnes = check_fitness(student, profession)
            # Выводим информацию
            print(f"Пригодность {check_fitnes['fit_percent']}.")
            print(f"{student['full_name']} знает {check_fitnes['has']}.")
            print(f"{student['full_name']} не знает {check_fitnes['lacks']}.")

        # Если профессия не найдена
        else:
            print("У нас нет такой специальности.")
            quit()
    # Если студент не найден
    else:
        print("У нас нет такого студента.")
        quit()
