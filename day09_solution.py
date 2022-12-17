with open("day09_input.txt") as f:
    motions = f.readlines()


def calculate_tail_position(direction, head, tail, head_knot):
    if head_knot:
        if direction == "R":
            head[0] += 1
        if direction == "L":
            head[0] -= 1
        if direction == "U":
            head[1] += 1
        if direction == "D":
            head[1] -= 1
    dist_x = abs(head[0]-tail[0])
    dist_y = abs(head[1]-tail[1])
    # case: head two steps directly up, down, left, or right from tail
    if dist_x > 1 and dist_y == 0:
        # head two steps left or right
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    elif dist_x == 0 and dist_y > 1:
        # head two steps up or down
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif dist_x > 1 and dist_y > 0:
        # head and tail aren't touching
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif dist_x > 0 and dist_y > 1:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    return head, tail


def collect_tail_visits_two_knots(positions, head, tail, visited):
    visited.add(str(tail))
    for line in positions:
        motion = line.strip().split(" ")
        direction = motion[0]
        steps = int(motion[1])
        for step in range(0, steps):
            head, tail = calculate_tail_position(direction, head, tail, head_knot=True)
            visited.add(str(tail))
    return len(visited)


def collect_tail_visits_ten_knots(positions, visited):
    knots = [[0, 0]]*10
    visited.add(str(knots[9]))
    for line in positions:
        motion = line.strip().split(" ")
        direction = motion[0]
        steps = int(motion[1])
        for step in range(0, steps):
            for idx in range(0, len(knots)-1):
                head = knots[idx].copy()
                tail = knots[idx+1].copy()
                is_head_knot = True if idx == 0 else False
                head, tail = calculate_tail_position(direction, head, tail, is_head_knot)
                if (idx + 1) == len(knots)-1:
                    visited.add(str(tail))
                knots[idx] = head
                knots[idx+1] = tail
    return len(visited)


# puzzle 1
# print(collect_tail_visits_two_knots(motions, [0, 0], [0, 0], set()))

# puzzle 2
print(collect_tail_visits_ten_knots(motions, set()))
