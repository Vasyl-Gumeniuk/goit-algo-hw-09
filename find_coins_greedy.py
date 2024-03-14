def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Error: {e}")
            return None
    return wrapper


@handle_errors
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        num_coin = amount // coin
        if num_coin > 0:
            change[coin] = num_coin
            amount -= num_coin * coin
        if amount == 0:
            break

    return change


def get_valid_amount_from_input():
    while True:
        try:
            amount_to_change = int(input("Введіть суму для здачі: "))
            if amount_to_change <= 0:
                print("Введено некоректне значення. Сума повинна бути більше нуля.")
            else:
                return amount_to_change
        except ValueError:
            print("Введено некоректні дані. Будь ласка, введіть ціле число.")


def main():
    amount_to_change = get_valid_amount_from_input()
    if amount_to_change is not None:
        print(find_coins_greedy(amount_to_change))
    



if __name__ == "__main__":
    main()
