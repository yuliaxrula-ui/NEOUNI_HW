import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[str, None, None]:
    """
    Аналізує текст і знаходить усі дійсні числа, відокремлені пробілами.
    Повертає ітератор (генератор) знайдених чисел у вигляді рядків.
    """
    # Шукає числа з крапкою або цілі числа, обмежені межами слів (\b)
    pattern = r"\b\d+\.\d+\b|\b\d+\b"
    
    # finditer дозволяє не завантажувати всі знахідки в пам'ять одразу
    for match in re.finditer(pattern, text):
        yield match.group()

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    """
    Обчислює загальну суму чисел у тексті, використовуючи функцію-генератор.
    """
    #sum() бере кожне число з генератора, перетворює на float і додає (можна було і через цикл for)
    return sum(float(number_str) for number_str in func(text))


text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

