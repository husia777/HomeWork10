from functions import *
from check_login import *


def main():
    while True:
        pk_input = input('Введите номер студента ')
        if pk_input == 'Выход':
            break
        try:
            student = get_student_by_pk(int(pk_input), load_students())
            print(f'Студент {student["full_name"]}\nЗнает {" ".join(student["skills"])}')
            correct_login(get_login(int(pk_input)))
            prof_input = input(f'Выберите специальность для оценки студента {student["full_name"]} ')
            if prof_input == 'Выход':
                break
            try:
                profession = get_profession_by_title(prof_input, load_professions())
                compliance_check = check_fitness(student, profession)
                print(f'Пригодность  {compliance_check["fit_percent"]} %')
                if compliance_check["has"] == 'Необходимых знаний нет':
                    print(f'{student["full_name"]}  {compliance_check["has"]}')
                else:
                    has = ' '.join(compliance_check["has"])
                    print(f'{student["full_name"]} знает {has}')

                if compliance_check["lacks"] == 'Нужные знания получены':
                    print(f'{student["full_name"]}  {compliance_check["lacks"]}')
                else:
                    lacks = ' '.join(compliance_check["lacks"])
                    print(f'{student["full_name"]} не знает {lacks}')
            except:
                print('У нас нет такой специальности')
        except:
            print('У нас нет такого студента')
            continue


if __name__ == '__main__':
    main()
