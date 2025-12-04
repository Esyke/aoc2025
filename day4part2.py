
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

def do_stuff2():
    removed_at_least_one_in_the_last_round = True
    total_moved_rolls = 0
    while removed_at_least_one_in_the_last_round:
        removed_at_least_one_in_the_last_round = False
        for i in range(len(diagram)):
            for j in range(len(diagram[i])):
                if diagram[i][j] == paper_roll:
                    if count_neighbouring_rolls(i, j) < 4:
                        diagram[i][j] = empty_space
                        removed_at_least_one_in_the_last_round = True
                        total_moved_rolls += 1
    return total_moved_rolls


def count_neighbouring_rolls(i, j):
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


def day4_part2():
    # read_file("day4small.txt")
    read_file("day4.txt")

    final_sum_2 = do_stuff2()
    # display_list(diagram)
    print("-----")

    print(final_sum_2)

if __name__ == "__main__":
    day4_part2()
