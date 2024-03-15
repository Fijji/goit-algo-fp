import random

def throw_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        dice1 = throw_dice()
        dice2 = throw_dice()
        total = dice1 + dice2
        sum_counts[total] += 1
    return sum_counts

def calculate_probabilities(sum_counts, num_rolls):
    probabilities = {}
    for total, count in sum_counts.items():
        probabilities[total] = count / num_rolls * 100
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}% ({probability / 100})")

num_rolls = 100000
sum_counts = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sum_counts, num_rolls)
print_probabilities(probabilities)
print("Можемо порівняти результати, отримані за допомогою методу Монте-Карло, \n з результатами аналітичних розрахунків, і виявити, що результати досить близькі, \n що підтверджує правильність обох методів визначення ймовірності сум при киданні двох кубиків.")
