from pathlib import Path

def get_cats_info(path) -> list:
    """Повертає список словників з іднтифікатором, імям та віком котів"""
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                id_item, name_item, age_item = line.strip().split(',')
                cats_dict = {"id": id_item, "name": name_item, "age": int(age_item)} #створюємо словник з одного рядка
                cats.append(cats_dict) #додаємо по одному словнику до списку
        return cats

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return [] # Повертаємо порожній список, щоб програма не зламалася
    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info(Path("cats_file.txt"))
    print(cats_info)