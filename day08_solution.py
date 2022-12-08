import sys

with open("day08_input.txt") as f:
    trees = f.readlines()


def populate_tree_grid(tree_input):
    grid = []
    for line in tree_input:
        t = [*line.strip()]
        grid.append(t)
    return grid


def count_visible_trees(grid_input):
    visible_trees = len(grid_input[0]) * 2 + (len(grid_input) - 2) * 2

    for idx in range(1, len(grid_input) - 1):
        for idy in range(1, len(grid_input[0]) - 1):
            curr_tree = int(tree_grid[idx][idy])
            # check top
            idt = idx - 1
            visible_top = True
            while idt >= 0:
                if int(grid_input[idt][idy]) >= curr_tree:
                    visible_top = False
                idt -= 1
            # check bottom
            idb = idx + 1
            visible_bottom = True
            while idb < len(grid_input):
                if int(grid_input[idb][idy]) >= curr_tree:
                    visible_bottom = False
                idb += 1
            # check left
            idl = idy - 1
            visible_left = True
            while idl >= 0:
                if int(grid_input[idx][idl]) >= curr_tree:
                    visible_left = False
                idl -= 1
            # check right
            idr = idy + 1
            visible_right = True
            while idr < len(grid_input[0]):
                if int(grid_input[idx][idr]) >= curr_tree:
                    visible_right = False
                idr += 1
            if visible_top or visible_bottom or visible_left or visible_right:
                visible_trees += 1
    return visible_trees


def calculate_scenic_score(grid_input):
    view_top, view_left, view_right, view_bottom = 0, 0, 0, 0
    max_scenic_score = -sys.maxsize
    for idx in range(1, len(grid_input)-1):
        for idy in range(1, len(grid_input[0])-1):
            curr_tree = int(tree_grid[idx][idy])
            # check top
            idt = idx - 1
            while idt >= 0:
                if int(grid_input[idt][idy]) >= curr_tree:
                    break
                idt -= 1
            if idt == -1:
                # hit an edge
                idt = 0
            view_top = abs(idx - idt)
            # check left
            idl = idy - 1
            while idl >= 0:
                if int(grid_input[idx][idl]) >= curr_tree:
                    break
                idl -= 1
            if idl == -1:
                idl = 0
            view_left = abs(idl - idy)
            # check right
            idr = idy + 1
            while idr < len(grid_input[0]):
                if int(grid_input[idx][idr]) >= curr_tree:
                    break
                idr += 1
            if idr == len(grid_input[0]):
                idr -= 1
            view_right = abs(idy - idr)
            # check bottom
            idb = idx + 1
            while idb < len(grid_input):
                if int(grid_input[idb][idy]) >= curr_tree:
                    break
                idb += 1
            if idb == len(grid_input):
                idb -= 1
            view_bottom = abs(idx - idb)
            scenic_score = view_top * view_left * view_right * view_bottom
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


tree_grid = populate_tree_grid(trees)

# puzzle 1
visible_tee_count = count_visible_trees(tree_grid)
# print(visible_tee_count)

# puzzle 2
print(calculate_scenic_score(tree_grid))
