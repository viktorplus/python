"""
Анализ продаж по категориям и датам
Пример запуска программы
python sales_report.py data/sales_data.txt reports
reports/
├── 2024/
│ ├── 12/
│ │ ├── monthly_report.txt
│ │ ├── Automotive.txt
├── 2025/
│ ├── 01/
│ │ ├── monthly_report.txt
│ │ ├── Clothing.txt
│ │ ├── Electronics.txt
│ ├── 02/
│ │ ├── monthly_report.txt
│ │ ├── Groceries.txt
│ │ ├── Sports.txt
"""

import sys  # доступ к argv и exit
from collections import defaultdict  # словарь с авто-значениями
from pathlib import Path  # удобная работа с путями/папками

def get_data_dicts(filename):  # читаем файл и возвращаем список словарей
    with open(filename, 'r', encoding='utf-8') as f:  # открываем файл в utf-8
        data = []  # список для всех продаж
        for line in f:  # перебираем строки файла
            name, date, amount, category, city = line.strip().split(",")  # парсим 5 полей
            year, month, day = date.split("-")  # делим дату на год/месяц/день
            data.append({  # добавляем запись как словарь
                "name": name,  # имя продавца
                "date": date,  # дата продажи
                "amount": amount,  # сумма продажи (строка)
                "category": category,  # категория товара
                "city": city,  # город
                "year": year,  # год из даты
                "month": month,  # месяц из даты
                "day": day  # день из даты
            })  # конец добавления записи
    return data  # возвращаем список продаж

def safe_filename(text):  # делаем безопасное имя файла из категории
    bad = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']  # запрещённые символы в именах файлов
    cleaned = "".join("_" if ch in bad else ch for ch in text).strip()  # заменяем плохие символы и чистим пробелы
    return cleaned if cleaned else "Unknown"  # если пусто — подставляем "Unknown"

def process_data(filename, output_dir):  # основная обработка + запись отчётов
    data = get_data_dicts(filename)  # получаем список продаж из файла

    by_year_month = defaultdict(lambda: defaultdict(int))  # (год,месяц)->(категория->сумма)
    lines_by_year_month = defaultdict(lambda: defaultdict(list))  # (год,месяц)->(категория->список строк)

    for sale in data:  # перебираем продажи
        year_month = (sale["year"], sale["month"])  # ключ группировки (год, месяц)
        category = sale["category"]  # категория текущей продажи
        amount = int(sale["amount"])  # сумма продажи как int

        by_year_month[year_month][category] += amount  # добавляем сумму в итог по категории
        lines_by_year_month[year_month][category].append((sale["date"], sale["name"], amount))  # сохраняем строку для файла категории

    out_root = Path(output_dir)  # корневая папка отчётов
    out_root.mkdir(parents=True, exist_ok=True)  # создаём корневую папку, если её нет

    for (year, month), cat_totals in by_year_month.items():  # перебираем каждый месяц (год/месяц)
        month_dir = out_root / year / month  # папка конкретного месяца: out/year/month
        month_dir.mkdir(parents=True, exist_ok=True)  # создаём папку месяца

        # print(f" {cat_totals}")
        # print(f" {cat_totals.values()}")
        #
        # print(f" {month_dir}")

        monthly_path = month_dir / "monthly_report.txt"  # путь к месячному отчёту
        full_sum = sum(cat_totals.values())  # общая сумма по всем категориям в месяце

        with monthly_path.open("w", encoding="utf-8", newline="\n") as f:  # открываем monthly_report.txt на запись
            for cat in sorted(cat_totals.keys()):  # категории сортируем по имени
                f.write(f"{cat},{cat_totals[cat]}\n")  # пишем строку "Category,Sum"
            f.write(f"Full,{full_sum}\n")  # пишем строку с итогом "Full,Total"

        for cat, rows in lines_by_year_month[(year, month)].items():  # перебираем продажи по категориям в месяце
            rows.sort(key=lambda x: x[0])  # сортируем записи по дате (YYYY-MM-DD)
            print(f" {cat}")
            print(f" {rows}")
            cat_file = month_dir / f"{safe_filename(cat)}.txt"  # путь к файлу категории
            with cat_file.open("w", encoding="utf-8", newline="\n") as f:  # открываем файл категории на запись
                for date_s, name, amount in rows:  # перебираем строки категории
                    f.write(f"{date_s},{name},{amount}\n")  # пишем "date,name,amount"

args = sys.argv  # берём аргументы командной строки
print(args)  # печатаем аргументы (для контроля)
if len(args) < 3:  # если аргументов меньше 3 (скрипт + input + output)
    print("Correct usage: python sales_report.py <input_file> <output_directory>")  # сообщение как запускать
    sys.exit(1)  # выходим с кодом ошибки 1

filename = args[1]  # путь к входному файлу
record_folder = args[2]  # путь к папке отчётов

process_data(filename, record_folder)  # запускаем обработку и генерацию отчётов
