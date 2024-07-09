from pathlib import Path

relative_path = Path('task_1/salary.txt')
absolute_path = relative_path.absolute()


def total_salary(path:str)->tuple[int, int] | None:
     total_salary = 0
     average = 0
     if path.exists():          
          with open(path, 'r', encoding='utf-8') as file:
               lines = file.readlines()
               for line in lines:
                    name, salary = line.split(',')
                    total_salary +=int(salary)

               if lines:
                    average = total_salary//len(lines)
                   
     else:
          print(f'Файлу за даним шляхом {path} не знайдено або він пошкоджений')
          return None

     return total_salary, average
    
          
          
result = total_salary(absolute_path)

if result:
     total, average = result
     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")