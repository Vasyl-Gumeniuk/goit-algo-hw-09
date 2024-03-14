import time

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

def measure_execution_time(algorithm, *args):
    start_time = time.time()
    algorithm(*args)
    end_time = time.time()
    return end_time - start_time

def test_algorithms():
    # Перевірка ефективності алгоритмів для різних сум
    test_amounts = [10, 50, 100, 500, 1000]
    for amount in test_amounts:
        greedy_time = measure_execution_time(find_coins_greedy, amount)
        dynamic_time = measure_execution_time(find_min_coins, amount)
        print(f"Amount: {amount}, Execution Time: {greedy_time:.10f} seconds (Greedy)")
        print(f"Amount: {amount}, Execution Time: {dynamic_time:.10f} seconds (Dynamic)\n")



def main():
    test_algorithms()



if __name__ == "__main__":
    main()
