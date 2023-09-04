# Работа с файлами\работа с ОС
import os
print(f'Текущая рабочая папка: {os.getcwd()}')
print(f'Текущий процесс: {os.getpid()}')
os.mkdir('temp_folder')  # Создание новой папки
os.rmdir('temp_folder')  # Удаление папки
# os.removedirs(r'temp_folder_1\temp_folder_2\temp_folder_3')
# os.makedirs(r'temp_folder_1\temp_folder_2\temp_folder_3')
with open('temp.txt', 'w') as f:
    f.write('hello, world!')

print(f'Перед удалением: {os.path.isfile("temp.txt")}, {os.path.exists("temp.txt")}')
os.remove('temp.txt')
print(f'После удаления: {os.path.isfile("temp.txt")}, {os.path.exists("temp.txt")}')
# Получение списка файлов
# glob - шаблон поиска
from pathlib import Path
import pprint
py_files = list(Path('.').glob('*.py'))
pprint.pprint(f'Python files: {py_files}')
for file in py_files:
    print(file.absolute())  # D:\PycharmProjects\nntu_march\new.py
    print(file.name)  # new.py
    print(file.suffix)  # .py
    print(file.stem)  # new

# Шаблон поиска glob
from glob import glob
# glob - создает списки имен, а Path.glob() создает пути
files = glob(r'D:\PycharmProjects\leet_code_solutions\*')
print(f'Файлы которые начинаются с lit: {files}')
files = glob('*')
print(f'Файлы которые начинаются с lit: {files}')

# Перемещение и копирование файлов
target_folder = Path("target_folder")  # создаем объект Path с именем (путь) новой папки
target_folder.mkdir(exist_ok=True)  # создаем саму папку
source_folder = Path('.')  # создаем путь до текущей папки
txt_files = source_folder.glob('*.txt')  # ищем все файлы с расширением .txt
for txt_files in txt_files:
    filename = txt_files.name  # берем имя файла
    target_path = target_folder.joinpath(filename)  # создаем новый путь <имя папки> + <имя файла>
    print(f'Перемещение файла...: {filename}')
    print(f'Существует ли до: {target_path.exists()}')  # проверяем существует ли файл
    txt_files.rename(target_path)  # перемещаем файл (меняем его путь)
    print(f'Существует ли после: {target_path.exists()}')

import shutil
source_file = "new_addresses.csv"  # имя старого файла
target_file = r"target_folder\new_addresses2.csv"  # имя + путь нового файла
target_file_path = Path(target_file)  # создаем путь к файлу target_folder\new_addresses2.csv
print(f'Существует ли файл перед копированием: {target_file_path.exists()}')  # проверка на существование
shutil.copy(source_file, target_file)  # копирование файла
print(f'Существует ли файл после копирования: {target_file_path.exists()}')  # проверка на существование


# Проверка директорий\файла
print(os.path.exists('target_folder'))  # существует ли папка target_folder True
print(Path('target_folder').exists())  # True
print(os.path.isdir('target_folder'))  # True
print(Path('lesson_11.py').is_dir())  # False
print(os.path.isfile('target_folder'))  # False
print(Path('lesson_10.py').is_file())  # True
