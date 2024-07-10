import sys
from pathlib import Path
from colorama import init, Fore, Style



def print_directory_structure(path:Path, separator ='')->None:
    try:    
        if not path.exists() or not path.is_dir():
            print(Fore.RED + 'Вказаний шлях не існує або не веде до директорії')
            return

        for item in path.iterdir():
            if item.is_dir():
                print(Fore.GREEN + separator + "📂 " + item.name )
                print_directory_structure(item, separator + '  ')
            else:
                print(Fore.BLUE + separator + '📜 ' + item.name)

    except Exception as e:
        print(Fore.RED + f'Помилка: {e}')


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(Fore.RED + 'Помилка: вкажіть шлях до директорії. Приклад введення: python3 hw03.py /шлях/до/вашої/директорії' + Style.RESET_ALL)
        return

    dir_path = Path(sys.argv[1])
    print_directory_structure(dir_path)



if __name__ == "__main__":
    main()