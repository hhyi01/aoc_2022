with open("day25_input.txt") as f:
    fuel = f.readlines()


def convert_to_decimal(snafu_numbers):
    symbols = {
        "-": -1,
        "=": -2
    }
    total_snafu = 0
    for line in snafu_numbers:
        fuel_line = [*line.strip()]
        fuel_line.reverse()
        digits = []
        curr_place = 1
        for i, d in enumerate(fuel_line):
            if d in symbols:
                curr_digit = curr_place * symbols[d]
            else:
                curr_digit = curr_place * int(d)
            digits.append(curr_digit)
            curr_place *= 5
        total_snafu += sum(digits)
    return total_snafu


def convert_to_snafu(decimal_number, base):
    symbols = {
        -1: "-",
        -2: "="
    }
    snafu_number = []
    exponent = get_exponent(decimal_number, base)
    curr_increment = base ** exponent
    snafu_val = 0
    while exponent >= 0:
        s = 0
        diff = snafu_val - decimal_number
        exponent -= 1
        next_increment = base ** exponent
        if diff == 0:
            snafu_number.append(str(s))
            break
        elif diff > 0:
            s, snafu_val = manage_gt_zero(snafu_val, decimal_number, curr_increment, next_increment, diff, s)
        else:
            s, snafu_val = manage_lt_zero(snafu_val, decimal_number, curr_increment, next_increment, diff, s)
        curr_increment = next_increment
        if s in symbols:
            snafu_number.append(str(symbols[s]))
        else:
            snafu_number.append(str(s))
    return "".join(snafu_number)


def manage_lt_zero(curr_snafu, dec_num, current_inc, next_inc, difference, step):
    while step < 2:
        if difference < (2 * next_inc)*-1 and current_inc*-1 > (2 * difference):
            curr_snafu += current_inc
            step += 1
            difference = curr_snafu - dec_num
        else:
            break
    return step, curr_snafu


def manage_gt_zero(curr_snafu, dec_num, current_inc, next_inc, difference, step):
    while step < 2:
        if difference > (2 * next_inc) and current_inc < (2 * difference):
            curr_snafu -= current_inc
            step += 1
            difference = curr_snafu - dec_num
        else:
            break
    return step*-1, curr_snafu


def get_exponent(val, base):
    exp = 0
    while base ** exp < val:
        exp += 1
    diff = (base ** exp) - (base ** (exp - 1))
    if (diff / val) > 2:
        exp -= 1
    return exp


# puzzle 1
# correct expression 2--2-0=--0--100-=210

dec_number = convert_to_decimal(fuel)
print(convert_to_snafu(dec_number, 5))



