with open("day06_input.txt") as f:
    datastream = f.readlines()


def subroutine(buffer, marker_length):
    curr_chars = []
    for idx, c in enumerate(buffer):
        if len(curr_chars) == marker_length:
            unique_chars = set(curr_chars)
            if len(unique_chars) == marker_length:
                return idx
            curr_chars = curr_chars[1:]
        curr_chars.append(c)
    return "No marker found."


# puzzle 1
print(subroutine(datastream[0], 4))

# puzzle 2
print(subroutine(datastream[0], 14))
