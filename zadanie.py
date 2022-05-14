Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
School = { }
for i in range(5):
  School.update( { input(f'Название класса № { i + 1 } : '): int(input(f'Количество учеников класса № { i + 1 } : ')) } )
print(School)
#B)
ClassName = input('Введите класс: ')
if ClassName in School:
  print(f'Количество учеников в классе { ClassName } : { School[ClassName] } ')
else:
  print('Такого класса на существует')
#C)
for i in range(3):
  School.update( { input(f'Название изменяемого класса { i + 1 } : '): int(input(f'Количество учеников изменяемого класса { i + 1 } : ')) } )
print(School)