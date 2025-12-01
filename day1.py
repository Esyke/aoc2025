import math
import re

full_sequence = list()
my_regex = r"(L|R)(\d+)"
start_pos = 50
seq_list = [50]

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            match = re.match(my_regex, next_line)
            full_sequence.append((match.groups()[0], match.groups()[1]))

def do_stuff(direction: str, how_far: int, initial_value: int):
    if direction == 'R':
        val = (initial_value + how_far)%100
    elif direction == 'L':
        val = (initial_value - how_far)%100
    else:
        print("NANI")
    seq_list.append(val)

def do_stuff2(direction: str, how_far: int, initial_value: int):
    if direction == 'R':
        val = initial_value + how_far
    elif direction == 'L':
        val = initial_value - how_far
    else:
        print("NANI")
    times_passed = 0
    if how_far == 0:
        times_passed = 0
    elif val == 0:
        times_passed = 1
    else:
        for i in range(initial_value+1, val+1):
            if i%100 == 0:
                times_passed+=1
        if val<0:
            for i in range(initial_value - 1, val - 1, -1):
                if i % 100 == 0:
                    times_passed += 1
    # print(f"{direction}{how_far} from {initial_value} - timespassed is {times_passed} at val {val}")
    seq_list.append(val%100)
    return times_passed

def day1_part1():
    read_file("day1.txt")
    for x in range(len(full_sequence)):
        do_stuff(full_sequence[x][0], int(full_sequence[x][1]), seq_list[x])
    final_sum_1 = seq_list.count(0)
    display_list(full_sequence)
    print("-----")
    display_list(seq_list)
    print("-----")

    print(final_sum_1)

def day1_part2():
    read_file("day1.txt")
    # read_file("day1small.txt")
    all_times_passed = 0
    for x in range(len(full_sequence)):
        all_times_passed+= do_stuff2(full_sequence[x][0], int(full_sequence[x][1]), seq_list[x])
    # display_list(full_sequence)
    print("-----")
    # display_list(seq_list)
    print("-----")

    print(all_times_passed)


if __name__ == "__main__":
    day1_part2()
