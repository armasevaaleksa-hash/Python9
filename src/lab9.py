# -*- coding: utf-8 -*-

"""
Інформаційний скрипт для Лабораторної роботи №9.

Цей файл не запускає веб-додаток безпосередньо.
Він надає інструкції, як запустити приклади для Flask та Django.

Будь ласка, дотримуйтесь інструкцій нижче.
"""

import os

def print_instructions():
    """
    Виводить інструкції для запуску прикладів Flask та Django.
    """
    flask_example_path = "flask_example"
    django_example_path = "django_example"

    print("="*80)
    print("Лабораторна робота № 9: Інструкції для запуску прикладів")
    print("="*80)
    print("\nЦей репозиторій містить два приклади веб-додатків: один на Flask, інший на Django.")
    print("Ви можете знайти їх у відповідних директоріях.\n")

    # --- Інструкції для Flask ---
    print("-" * 30 + " Flask Example " + "-" * 31)
    print(f"Приклад знаходиться в директорії: {flask_example_path}/\n")
    print("Щоб запустити його, виконайте наступні команди з директорії 'src':\n")
    print(f"1. Перейдіть до директорії з прикладом:")
    print(f"   cd {flask_example_path}\n")
    print(f"2. Запустіть додаток:")
    print(f"   python app.py\n")
    print("Після запуску, додаток буде доступний за адресою: http://127.0.0.1:5000\n")

    # --- Інструкції для Django ---
    print("-" * 30 + " Django Example " + "-" * 30)
    print(f"Приклад знаходиться в директорії: {django_example_path}/\n")
    print("Щоб запустити його, виконайте наступні команди з директорії 'src':\n")
    print(f"1. Перейдіть до директорії з прикладом:")
    print(f"   cd {django_example_path}\n")
    print(f"2. Застосуйте міграції бази даних (це потрібно зробити один раз):")
    print(f"   python manage.py migrate\n")
    print(f"3. Запустіть сервер для розробки:")
    print(f"   python manage.py runserver\n")
    print("Після запуску, додаток буде доступний за адресою: http://127.0.0.1:8000\n")
    print("="*80)


if __name__ == '__main__':
    # Перевіряємо, чи скрипт запускається з директорії `src`
    current_dir = os.path.basename(os.getcwd())
    if current_dir != 'src':
        print(f"\n[ПОПЕРЕДЖЕННЯ] Будь ласка, запустіть цей скрипт з директорії 'src', щоб шляхи були правильними.")
        print(f"Поточна директорія: {os.getcwd()}\n")

    print_instructions()