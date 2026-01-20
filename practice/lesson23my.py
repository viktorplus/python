
from typing import List, Dict

def get_words_with_len(words_data: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words_data}

words = ["apple", "banana", "cherry"]
print(get_words_with_len(words))

# -----------------

name = "Alice"
achievements = ["Won chess tournament", "Completed marathon", "Published a book"]
# Пример вывода:
#
# Alice: Won chess tournament, Completed marathon, Published a book
def get_name_achievements(name:str, achievements: list[str] | None = None) -> str:

    if achievements:
        return f"{name} achievements: {', '.join(achievements)}"
    return "No achievements"
print(get_name_achievements(name, achievements))
print(get_name_achievements(name))

# ------------------

def is_even(num: int) -> bool:
    return num % 2 == 0

from typing import Callable

def filter_by(predicat: Callable[[int], bool], nums: list[int]) -> list[int]:
    return [num for num in nums if predicat(num)]
nums = [1, 2, 3, 4, 5]
print(filter_by(is_even, nums))


# Агрегирование списка
# Вычислите произведение всех элементов списка с помощью функции высшего порядка.
# Данные:
numbers = [1, 2, 3, 4, 5]
# Пример вывода:
# 120
from functools import reduce
from typing import Iterable
def count_get_multiple(numbers: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, numbers)
print(count_get_multiple(numbers))