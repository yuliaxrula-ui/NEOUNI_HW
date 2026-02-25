import random


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:
    """
    Генерує набір унікальних випадкових чисел для лотерейного квитка.

    Аргументи:
        min_val (int): Мінімальне число в діапазоні (не менше 1).
        max_val (int): Максимальне число в діапазоні (не більше 1000 і не менше 0).
        quantity (int): Кількість чисел, які потрібно вибрати.

    Повертає:
        list: Відсортований список випадкових чисел або порожній список при помилці.
    """
    # Перевірка типів
    if not (isinstance(min_val, int) and isinstance(max_val, int) and isinstance(quantity, int)):
        return []

    # Перевірка логічних меж
    if (min_val < 1) or (0 > max_val > 1000) or (quantity < 0) or (quantity > (max_val - min_val + 1)):
        return []

    # range працює з min_val та max_val
    lottery_range = range(min_val, max_val + 1)
    win_num = random.sample(lottery_range, k=quantity)
    
    return sorted(win_num)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)