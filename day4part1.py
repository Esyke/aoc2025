
diagram = list()
paper_roll = "@"
empty_space = "."


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            diagram.append(list(next_line.strip()))

def do_stuff():
    movable_rolls = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == paper_roll:
                if count_neighbours(i, j) < 4:
                    movable_rolls += 1
    return movable_rolls


def count_neighbours(i, j):
    roll_count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if is_valid_coordinate(x, y):
                if diagram[x][y] == paper_roll:
                    roll_count += 1
    return roll_count

def is_valid_coordinate(i, j):
    if 0<=i<len(diagram):
        if 0<=j<len(diagram[i]):
            return True
    return False

def day4_part1():
    # read_file("day4small.txt")
    read_file("day4.txt")

    final_sum_1 = do_stuff()
    # display_list(diagram)
    print("-----")

    print(final_sum_1)

if __name__ == "__main__":
    day4_part1()
