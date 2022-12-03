with open("day03_input.txt") as f:
    rucksacks = f.readlines()

items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def populate_priorities(items_list, priorities_dict):
    for idx, item in enumerate(items_list):
        priorities_dict[item] = idx + 1
    return priorities_dict


def calculate_priorities_sum(items_list, priorities_dict):
    total = 0
    for item in items_list:
        total += priorities_dict[item]
    return total


def get_erroneous_items(rucksack_list):
    erroneous_items = []
    for line in rucksack_list:
        rucksack = line.strip()
        separator = int(len(rucksack)/2)
        compartment1 = {*rucksack[:separator]}
        compartment2 = {*rucksack[separator:]}
        erroneous_item = list(compartment1.intersection(compartment2))[0]
        erroneous_items.append(erroneous_item)
    return erroneous_items


def get_badge_items(rucksack_list, n):
    badges = []
    elf_group = []
    if len(rucksack_list) % n != 0:
        return "Bad divisor."
    for idx, line in enumerate(rucksack_list):
        rucksack = line.strip()
        if idx % n == 0:
            if len(elf_group) == n:
                badge = list(elf_group[0].intersection(*elf_group))[0]
                badges.append(badge)
            elf_group = [{*rucksack}]
        else:
            elf_group.append({*rucksack})
    badge = list(elf_group[0].intersection(*elf_group))[0]
    badges.append(badge)
    return badges


priorities = populate_priorities(items, {})
err_items = get_erroneous_items(rucksacks)

# puzzle 1
print(calculate_priorities_sum(err_items, priorities))

# puzzle 2
badges_list = get_badge_items(rucksacks, 3)
print(calculate_priorities_sum(badges_list, priorities))

