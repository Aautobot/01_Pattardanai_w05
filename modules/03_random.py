import random
# print(f"{random.random()}")
# print(f"{random.randint(1, 10)}")  # Random integer between 1 and 10
# print(f"{random.randrange(1, 10, 2)}")  # Random odd number between 1 and 9
# print(f"{random.uniform(1.0, 10.0)}")  # Random float between 1.0 and 10.0

colors = ["red", "green", "blue", "yellow", "purple"]
# random_color = random.choice(colors)  # Randomly select a color from the list
# random_3 = random.choices(colors,k=3)  # Randomly select 3 colors from the list
# print(f"Randomly selected colors: {random_3}")
random_unique = random.sample(colors, 3)  # Randomly select 3 unique colors from the list
print(f"Randomly selected unique colors: {random_unique}")
# print(f"Randomly selected color: {random_color}")
# print(f"{random.choice(colors)}")  # Randomly select a color from the list
# print(f"{random.sample(colors, 3)}")  # Randomly select 3 colors from the list
# random.shuffle(colors)  # Shuffle the list of colors
# print(f"{colors}")  # Print the shuffled list of colors

numbers = list(range(1, 100))  # Create a list of numbers from 1 to 100
# print(f"{random.choice(numbers)}")  # Randomly select a number from the list
# print(f"{random.sample(numbers, 5)}")  # Randomly select 5 unique numbers from the list
random.shuffle(numbers)  # Shuffle the list of numbers
print(f"{numbers}")  # Print the shuffled list of numbers
