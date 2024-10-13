import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Копіювання та сортування файлів за розширенням.')
    parser.add_argument('source_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    return parser.parse_args()

def copy_files_recursively(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        if os.path.isdir(item_path):
            try:
                copy_files_recursively(item_path, dest_dir)
            except Exception as e:
                print(f'Помилка при обробці директорії {item_path}: {e}')
        else:
            file_extension = os.path.splitext(item)[1].lower()  # Отримуємо розширення файлу
            target_dir = os.path.join(dest_dir, file_extension[1:] if file_extension else 'no_extension')

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            try:
                shutil.copy2(item_path, target_dir)
                print(f'Копіювання файлу {item_path} до {target_dir}')
            except Exception as e:
                print(f'Помилка при копіюванні файлу {item_path}: {e}')

def main():
    args = parse_arguments()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    if not os.path.exists(source_dir):
        print(f'Вихідна директорія {source_dir} не існує.')
        return

    copy_files_recursively(source_dir, dest_dir)
    print('Копіювання та сортування файлів завершено.')

if __name__ == '__main__':
    main()
