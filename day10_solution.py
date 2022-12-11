with open("day10_input.txt") as f:
    program = f.readlines()


def execute_program(instructions, imp_sig):
    x = 1
    cycle = 1
    add = []
    sum_signal_strengths = 0
    crt_pixels = []
    for line in instructions:
        instruction = line.strip().split(" ")
        if len(add) > 0:
            prev_instruction = add.pop()
            x += prev_instruction
        if len(instruction) > 1:
            add.append(int(instruction[1]))
        else:
            add.append(0)
        command = instruction[0]

        if command == "noop":
            cycle_to_complete = cycle + 1
        else:
            cycle_to_complete = cycle + 2

        while cycle < cycle_to_complete:
            print("Executing: ", " ".join(instruction), " Cycle: ", cycle, " Current x: ", x)
            if cycle in imp_sig:
                sum_signal_strengths += cycle * x
            if x-1 <= (cycle-1) % 40 <= x+1:
                crt_pixels.append("#")
            else:
                crt_pixels.append(".")
            cycle += 1

    last_instruction = add.pop()
    x += last_instruction
    if cycle in imp_sig:
        sum_signal_strengths += cycle * x

    print("".join(crt_pixels[:39]))
    print("".join(crt_pixels[40:79]))
    print("".join(crt_pixels[80:119]))
    print("".join(crt_pixels[120:159]))
    print("".join(crt_pixels[160:199]))
    print("".join(crt_pixels[200:239]))

    return sum_signal_strengths


# puzzle 1 & puzzle 2
signal_strengths = {20, 60, 100, 140, 180, 220}
print(execute_program(program, signal_strengths))
