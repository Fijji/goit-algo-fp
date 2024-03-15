def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_data in sorted_items:
        if total_cost + item_data['cost'] <= budget:
            selected_items.append(item_name)
            total_cost += item_data['cost']
            total_calories += item_data['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i, (item_name, item_data) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if item_data['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_data['cost']] + item_data['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]['cost']

    return selected_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані продукти:", selected_items_greedy)
print("Всього калорій:", total_calories_greedy)

# Використання алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Обрані продукти:", selected_items_dp)
print("Всього калорій:", total_calories_dp)
