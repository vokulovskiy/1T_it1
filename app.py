import os
from datetime import datetime

# Задание пути
# path = "C:/users/"  # Задайте путь здесь (закомментируйте для использования корневого каталога)
try:
    if os.path.isdir(path):
        pass
except:
    path = os.path.abspath(os.sep)  # По умолчанию — корневой каталог файловой системы

def get_top_10_largest_files(directory):
    """Вычисляет количество файлов в заданном каталоге (и подкаталогах)."""
    file_count = 0
    """Возвращает топ-10 файлов по размеру в заданном каталоге (и подкаталогах)."""
    files_with_sizes = []
    for root, dirs, files in os.walk(directory):
        if root != path:
            break
        file_count += len(files)
        for file in files:
            try:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path) / 1024  # Размер в Кб
                files_with_sizes.append((file_path, size))
            except OSError:
                # Игнорируем ошибки доступа
                continue
    # Сортировка по размеру (в порядке убывания)
    files_with_sizes.sort(key=lambda x: x[1], reverse=True)
    return file_count, files_with_sizes[:10]

def greet_user(name):
    """Выводит приветствие с указанным именем и текущей датой/временем."""
    now = datetime.now()
    print(f"Привет, {name}! Сегодня {now.strftime('%d.%m.%Y %H:%M:%S')}.")

if __name__ == "__main__":
    user = os.getenv("USER", "Stranger")

    # Приветствие
    greet_user(user)

    file_count, largest_files = get_top_10_largest_files(path)

    # Вывод количества файлов
    print(f"Количество файлов в каталоге '{path}': {file_count}")

    # Вывод топ-10 файлов по размеру
    print("\nТоп-10 самых больших файлов (в Кб):")
    for i, (file_path, size) in enumerate(largest_files, start=1):
        print(f"{i}. {file_path} — {size:.2f} Кб")
