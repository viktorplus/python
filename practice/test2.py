import re
text = """
Orders: ID123, ID4567, ID89
Numbers: 123-45-67, 321-45-67
Prices: 100$, 199.50$, 99.99€, 0.49€, .99€
File names: report.txt, report2.txt, report10.txt
"""
print("Одна или более цифр:", re.findall(r"\d+", text))
print("Телефонные номера (формата xxx-xx-xx):", re.findall(r"\d{3}-\d{2}-\d{2}", text))
print("Цены (числа с десятичной точкой):", re.findall(r"\d+\.\d+", text))
print("ID-коды:", re.findall(r"ID\d{2,}", text))
print("Имена файлов 0+ цифр:", re.findall(r"report\d*.txt", text))
print("Имена файлов 0/1 цифр:", re.findall(r"report\d?.txt", text))
print("Имена файлов 1/2 цифр:", re.findall(r"report\d{1,2}.txt", text))