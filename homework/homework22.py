"""Python Fundamentals 2025: Домашнее задание 22

1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.

Пример вывода:
['Chair', 'Laptop']
Данные:
"""


# def large_orders(saleslist):
#     return sorted([d["product"] for d in saleslist if d["price"] > 500])
#
#     # return sorted(
#     #     map(lambda d: d["product"],
#     #         filter(lambda d: d["price"] > 500, saleslist)
#     #         )     )
#
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
#
# print(large_orders(orders))



"""2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
Данные:"""

def by_revenue(x):
    return x[1]

def revenue_by_goods(sales_list):
    revenue = {}

    for product, qty, price in sales_list:
        revenue[product] = qty * price

    return dict(
        # sorted(revenue.items(), key=lambda x: x[1], reverse=True)
        sorted(revenue.items(), key=by_revenue, reverse=True)
    )


sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

print (revenue_by_goods(sales))
