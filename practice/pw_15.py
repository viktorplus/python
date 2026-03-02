# Реализуйте программу, которая должна:
# Прочитать данные из JSON-файла.
# Для каждого ученика и предмета вычислить среднюю оценку за каждый учебный квартал:
# 1 квартал: январь–март
# 2 квартал: апрель–май (лето пропускается)
# 3 квартал: сентябрь–декабрь
# Записать результаты в новый JSON-файл, сгруппированные по ученикам, предметам и кварталам.
#
# Пример вывода
# quarterly_report.json
#
# {
#     "Bob": {
#         "Science": {
#             "Q1": 86.0
#         },
#         "Literature": {
#             "Q1": 94.0,
#             "Q2": 68.0,
#             "Q3": 81.0
#         },
#         "History": {
#             "Q1": 73.67
#         }
#     },
import json
from collections import defaultdict
from datetime import datetime

def get_quarter(date_str):
    month = datetime.strptime(date_str, "%d-%m-%Y").month
    if month in [9,10,11]:
        return "Q1"
    elif month in [12,1,2]:
        return "Q2"
    elif month in [3,4,5]:
        return "Q3"

# print(get_quarter("10-11-2026"))

with open("grades.json","r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)


grouped_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

for d in data:
    name = d["name"]
    grade = d["grade"]
    subject = d["subject"]
    date = d["date"]
    quarter = get_quarter(date)
    if quarter:
        grouped_data[name][subject][quarter].append(grade)
print(grouped_data)


report = {}
for name, subjects in grouped_data.items():
    report[name] = {}
    for subject, quarters in subjects.items():
        report[name][subject] = {}
        for quarter, grades in quarters.items():
            report[name][subject][quarter] = round(sum(grades) / len(grades))
print(report)

with open("report.json","w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)














