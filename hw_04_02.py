import random
def get_numbers_ticket(min, max, quantity):
    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        return []
    elif (min<1) or (max>1000) or (quantity > (max - min + 1)):
        return []
    else:
        lottery_range=list(range(min, max + 1))
        win_num=sorted(random.sample(lottery_range,k=quantity),reverse=False)
        return win_num
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)