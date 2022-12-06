with open("day05_input.txt") as f:
    supply_details = f.readlines()


def parse_stacks(supply_input):
    supply_stacks_dict = {}
    for line in supply_input:
        if line.strip().startswith("1"):
            stacks = line.strip().split("  ")
            for s in stacks:
                stack_id = int(s.strip())
                supply_stacks_dict[stack_id] = []
    return supply_stacks_dict


def parse_crates(supply_input, supply_dict):
    crates = []
    stack_count = len(supply_dict)
    for line in supply_input:
        if line.strip().startswith("1"):
            return crates
        space_count = 0
        stack = []
        for c in line.split(" "):
            if space_count == 4:
                stack.append("")
                space_count = 0
            if c == "":
                space_count += 1
            else:
                stack.append(c.strip())
        if len(stack) < stack_count:
            stack += [""]*(stack_count-len(stack))
        crates.append(stack)


def populate_supply_stacks(crates_list, supply_dict):
    for stack_id in supply_dict:
        for crate in crates_list:
            if crate[stack_id-1] != "":
                supply_dict[stack_id].append(crate[stack_id-1])
        if len(supply_dict[stack_id]) > 0:
            supply_dict[stack_id] = list(reversed(supply_dict[stack_id]))
    return supply_dict


def rearrange_crates(supply_input, stacks_filled):
    for line in supply_input:
        if line.strip().startswith("move"):
            instruction = line.strip().split(" ")
            num_to_move = int(instruction[1])
            stack_to_take_from = int(instruction[3])
            stack_to_add_to = int(instruction[len(instruction)-1])
            for i in range(0, num_to_move):
                crate = stacks_filled[stack_to_take_from].pop()
                stacks_filled[stack_to_add_to].append(crate)
    return stacks_filled


def get_top_each_stack(stacks_rearranged):
    top_crates = []
    for stack in stacks_rearranged:
        top_crates.append(stacks_rearranged[stack].pop())
    return "".join(top_crates).replace("[", "").replace("]", "")


def rearrange_crates_9001(supply_input, stacks_filled):
    for line in supply_input:
        if line.strip().startswith("move"):
            instruction = line.strip().split(" ")
            num_to_move = int(instruction[1])
            stack_to_take_from = int(instruction[3])
            stack_to_add_to = int(instruction[len(instruction)-1])
            crates = stacks_filled[stack_to_take_from][num_to_move*-1:]
            stacks_filled[stack_to_add_to].extend(crates)
            stacks_filled[stack_to_take_from] = stacks_filled[stack_to_take_from][:len(stacks_filled[stack_to_take_from])-num_to_move]
    return stacks_filled


supply_stacks_empty = parse_stacks(supply_details)
crates_from_top = parse_crates(supply_details, supply_stacks_empty)
supply_stacks_filled = populate_supply_stacks(crates_from_top, supply_stacks_empty)

# puzzle 1
# rearranged_stacks = rearrange_crates(supply_details, supply_stacks_filled)
# print(get_top_each_stack(rearranged_stacks))

# puzzle 2
rearranged_stacks_9001 = rearrange_crates_9001(supply_details, supply_stacks_filled)
print(get_top_each_stack(rearranged_stacks_9001))
