import itertools

all_red_coordinates = list()

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            all_red_coordinates.append((int(next_line.split(",")[0]), int(next_line.split(",")[1])))

def find_max_size_rectangle():
    max_rectangle = 0
    for pair in itertools.combinations(all_red_coordinates, 2):
        current_rectangle_size = (abs(pair[0][0]-pair[1][0])+1)*(abs(pair[0][1]-pair[1][1])+1)
        if current_rectangle_size > max_rectangle:
            max_rectangle = current_rectangle_size
    return max_rectangle

def day9_part1():
    # read_file("day9small.txt")
    read_file("day9.txt")
    # display_list(all_red_coordinates)
    final_sum_1 = find_max_size_rectangle()
    print("-----")

    print(final_sum_1)

if __name__ == "__main__":
    day9_part1()
