def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Error: {e}")
            return None
    return wrapper


@handle_errors
def find_min_coins(amount, memo=None):
    if memo is None:
        memo = {}
    if amount <= 0:
        return {} if amount == 0 else None
    if amount in memo:
        return memo[amount]

    coins = [50, 25, 10, 5, 2, 1]
    min_coins = float('inf')
    best_change = None
    for coin in coins:
        change = find_min_coins(amount - coin, memo)
        if change is not None and len(change) + 1 < min_coins:
            min_coins = len(change) + 1
            best_change = change.copy()
            best_change[coin] = best_change.get(coin, 0) + 1

    memo[amount] = best_change
    return best_change


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
        print(find_min_coins(amount_to_change))



if __name__ == "__main__":
    main()
