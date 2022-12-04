with open("day04_input.txt") as f:
    sections = f.readlines()


def section_contains_other(section1, section2):
    endpoints1 = section1.split("-")
    endpoints2 = section2.split("-")
    is_overlapping = int(endpoints1[0]) >= int(endpoints2[0]) and int(endpoints1[1]) <= int(endpoints2[1]) or \
                     int(endpoints2[0]) >= int(endpoints1[0]) and int(endpoints2[1]) <= int(endpoints1[1])
    return is_overlapping


def expand_section(section):
    expanded = set()
    endpoints = section.split("-")
    start = int(endpoints[0])
    end = int(endpoints[1])
    for i in range(start, end+1):
        expanded.add(i)
    return expanded


def containment_count(sections_list):
    total = 0
    for line in sections_list:
        parts = line.strip().split(",")
        overlaps = section_contains_other(parts[0], parts[1])
        if overlaps:
            total += 1
    return total


def overlap_count(sections_list):
    total = 0
    for line in sections_list:
        parts = line.strip().split(",")
        section1 = expand_section(parts[0])
        section2 = expand_section(parts[1])
        overlap = section1.intersection(section2)
        if len(overlap) > 0:
            total += 1
    return total


# puzzle 1
print(containment_count(sections))

# puzzle 2
print(overlap_count(sections))
