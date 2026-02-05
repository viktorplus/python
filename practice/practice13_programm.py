"""Задание
Анализ продаж по категориям и датам
Напишите программу, которая обрабатывает текстовый файл с данными о продажах.
Используйте файл sales_data.txt.

Программа должна
1. Принимать аргументы командной строки:
python sales_report.py <input_file> <output_directory>
Где:
○ <input_file> — путь к входному файлу с продажами.
○ <output_directory> — папка, куда будут сохранены отчёты.

2. Считать данные из текстового файла, в котором каждая строка содержит информацию в следующем
формате:
имя,дата,сумма,категория,город
Пример входных данных:
Olivia Suarez,2024-08-02,4565,Electronics,Dallas
Jennifer Jacobs,2023-08-19,4963,Automotive,London
Erin Johnson,2024-08-29,1796,Clothing,Miami

3. Сгруппировать данные по годам и месяцам, создавая для каждого года и месяца отдельную папку в
указанной директории.

4. Создать общий отчёт по каждому месяцу (monthly_report.txt), в котором указана суммарная выручка по
каждой категории и общая сумма:
Automotive,109539
Books,133160
Clothing,102001
Electronics,79403
Groceries,104387
Home Appliances,99911
Sports,78782
Full,707183

5. Создать файлы для каждой категории товаров, в которых должны быть указаны все продажи по данной
категории в формате:
дата,имя продавца,сумма
Пример файла Electronics.txt:
2025-02-01,Cynthia Maddox,538
2025-02-01,Kendra Martinez,3799
2025-02-02,Rachel Miller,1097
Все записи в файле должны быть отсортированы по дате.

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
import sys
from collections import defaultdict


def get_data_dicts(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            name, date, amount, category, city = line.strip().split(",")
            year, month, day = date.split("-")
            data.append({
                "name": name,
                "date": date,
                "amount": amount,
                "category": category,
                "city": city,
                "year": year,
                "month": month,
                "day": day
            })
    return data

def process_data(filename):
    data = get_data_dicts(filename)
    # {(year,month) : {category : int}}
    by_year_month = defaultdict(lambda: defaultdict (int))
    for sale in data:
        year_month = (sale["year"], sale["month"])
        category = sale["category"]
        amount = int(sale["amount"])
        by_year_month[year_month][category] += amount
    print(by_year_month)


args = sys.argv
print(args)
if len(args) < 3:
    print("Correct usage: python sales_report.py <input_file> <output_directory>")
    sys.exit(1)
filename = args[1]
record_folder = args[2]

process_data(filename)
#print(*get_data_dicts(filename), sep="\n")





