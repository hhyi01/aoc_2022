import math

with open("day11_input.txt") as f:
    input_lines = f.readlines()


def parse_monkeys(lines):
    monkey_list = []
    tests = []

    for idx, line in enumerate(lines):
        if line.strip().startswith("Monkey"):
            monkey = {}
            for i in range(1, 6):
                prop = lines[idx+i].strip().split(":")
                prop_name = prop[0]
                if prop_name.startswith("Starting"):
                    items = prop[1].replace(" ", "").split(",")
                    starting_items = [int(item) for item in items]
                    monkey[prop_name] = starting_items
                else:
                    monkey[prop_name] = prop[1].strip()
                    if prop_name == "Test":
                        test = monkey[prop_name].split(" ")
                        divider = int(test[len(test)-1])
                        tests.append(divider)
            monkey_list.append(monkey)
    return monkey_list, tests


def monkey_rounds_v1(monkey_list, rounds):
    ops = {
        "*": "multiply",
        "+": "add"
    }
    inspection_count = [0]*len(monkey_list)

    for r in range(1, rounds+1):
        for i, monkey in enumerate(monkey_list):
            print("Observing Monkey", i)
            if len(monkey["Starting items"]) > 0:
                for item in monkey["Starting items"]:
                    print("Monkey", i, "inspecting", item)
                    old = item
                    op = monkey["Operation"].split(" ")
                    action = ops[op[3]]
                    worry = int(op[4]) if op[4] != "old" else old
                    new_worry_level = (old + worry) if action == "add" else (old * worry)
                    print("New worry level:", new_worry_level)
                    print("Monkey", i, "gets bored with item.")
                    curr_worry_level = math.floor(new_worry_level/3)
                    print("Current worry level:", curr_worry_level)
                    print("Testing worry is", monkey["Test"])
                    test = int(monkey["Test"].split(" ")[2])
                    throw_monkey = int(monkey["If true"].split(" ")[3]) if curr_worry_level % test == 0 else \
                        int(monkey["If false"].split(" ")[3])
                    monkey_list[throw_monkey]["Starting items"].append(curr_worry_level)
                    if curr_worry_level % test == 0:
                        print(monkey["If true"])
                    else:
                        print(monkey["If false"])
                    inspection_count[i] += 1
                print("Monkey", i, "threw all the items.")
                monkey_list[i]["Starting items"] = []

        print("Standing at the end of round", r)
        for n, m in enumerate(monkey_list):
            print("Monkey", n, ":", monkey_list[n]["Starting items"])

        print("Round:", r, "Number of inspections per Monkey:", inspection_count)

    inspection_count.sort(reverse=True)
    return inspection_count[:2]


def multiply_list(test_numbers):
    product = 1
    for test_number in test_numbers:
        product = product * test_number
    return product


def monkey_rounds_v2(monkey_list, tests, rounds):
    ops = {
        "*": "multiply",
        "+": "add"
    }
    inspection_count = [0]*len(monkey_list)
    test_factor = multiply_list(tests)

    for r in range(1, rounds+1):
        for i, monkey in enumerate(monkey_list):
            if len(monkey["Starting items"]) > 0:
                for item in monkey["Starting items"]:
                    old = item
                    op = monkey["Operation"].split(" ")
                    action = ops[op[3]]
                    worry = int(op[4]) if op[4] != "old" else old
                    new_worry_level = (old + worry) if action == "add" else (old * worry)
                    curr_worry_level = new_worry_level % test_factor
                    test = int(monkey["Test"].split(" ")[2])
                    throw_monkey = int(monkey["If true"].split(" ")[3]) if curr_worry_level % test == 0 else \
                        int(monkey["If false"].split(" ")[3])
                    monkey_list[throw_monkey]["Starting items"].append(curr_worry_level)

                    inspection_count[i] += 1
                monkey_list[i]["Starting items"] = []

        print("Round:", r, "Number of inspections per Monkey:", inspection_count)

    inspection_count.sort(reverse=True)
    return inspection_count[:2]


# puzzle 1
monkeys, tests_list = parse_monkeys(input_lines)
# most_active_two = monkey_rounds_v1(monkeys, 20)
# print(most_active_two[0]*most_active_two[1])

# puzzle 2
most_active_two = monkey_rounds_v2(monkeys, tests_list, 10000)
print(most_active_two[0]*most_active_two[1])
