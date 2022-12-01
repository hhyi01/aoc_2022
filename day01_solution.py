with open("day01_input.txt") as f:
    content = f.readlines()


max_calories = 0
calories = 0

calories_list = []

for line in content:
    if line != "\n":
        calories += int(line.strip())
    else:
        if calories > max_calories:
            max_calories = calories
        calories_list.append(calories)
        calories = 0
calories_list.append(calories)

# puzzle 1
print(max_calories)

# puzzle 2
calories_list.sort()
print(sum(calories_list[-3:]))

