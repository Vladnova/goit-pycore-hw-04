from pathlib import Path
from typing import List

relative_path = Path('task_2/cats.txt')
absolute_path = relative_path.absolute()


def get_cats_info(path:str)->List | None:
    res = []
    
    if path.exists():          
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
               id, name, age = line.strip().split(',')
               res.append({'id':id, 'name':name, 'age':age})
              
                  
    else:
        print(f'Файлу за даним шляхом {path} не знайдено або він пошкоджений')
        
    return res or None
    
          
          
cats_info = get_cats_info(absolute_path)

print(cats_info)