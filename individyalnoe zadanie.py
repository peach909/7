Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
 
if __name__ == '__main__':
    students = []
 
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <средний балл> - запросить студентов с баллом выше 4.0;")
    print("exit - завершить работу с программой.")
 
    while True:
        command = input(">>> ").lower()
 
        if command == 'exit':
            break
        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            grade = list(map(int, input("Успеваемость ").split()))
            student = {
                'name': name,
                'group': group,
                'grade': grade,
            }
            students.append(student)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))
 
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)
 
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('grade', 0)
                    )
                )
            print(line)
        elif command.startswith('select '):
            count = 0
            for student in students:
                if "4" in student.get('grade', ''):
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, student.get('name', '')),
                        '{:>1} {}'.format('группа №', student.get('group', ''))
                    )
         if count == 0:
     print("Студенты с баллом 4.0 и выше не найдены.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)