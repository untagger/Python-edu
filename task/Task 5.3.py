from calendar import day_name


def request_day_number() -> int:
    while True:
        try:
            value = int(input(
                "Введите день недели: "
            ))
        except ValueError:
            print("Неправильный ввод, введите цифры: ")
            continue

        if 1 <= value <= 7:
            return value
        print("Такого дня недели не существует, попробуй еще: ")


def main():
    day_no = request_day_number()
    name = day_name[day_no - 1]
    print(f'Day {day_no} is {name}')


if __name__ == '__main__':
    main()