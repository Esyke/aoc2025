import re

fresh_range_regex = r"(\d+)-(\d+)"
all_id_ranges = list()
unique_id_ranges = list()


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if re.match(fresh_range_regex, next_line):
                match = re.match(fresh_range_regex, next_line)
                all_id_ranges.append((int(match.groups()[0]), int(match.groups()[1])))
            else:
                break


def do_stuff2():
    #its sorted so the next range's start can never be smaller than the last range's start
    unique_id_ranges.append(all_id_ranges[0][0])
    unique_id_ranges.append(all_id_ranges[0][1])
    for index in range(1, len(all_id_ranges)):
        if unique_id_ranges[-2] <= all_id_ranges[index][0] <= unique_id_ranges[-1]:
            if unique_id_ranges[-1] < all_id_ranges[index][1]:
                unique_id_ranges[-1] = all_id_ranges[index][1]
            else:
                continue
        else:
            unique_id_ranges.append(all_id_ranges[index][0])
            unique_id_ranges.append(all_id_ranges[index][1])


def count_ranges():
    elements_in_ranges = 0
    for i in range(0, len(unique_id_ranges), 2):
        elements_in_ranges += (unique_id_ranges[i + 1] - unique_id_ranges[i] + 1 )
    return elements_in_ranges

def day5_part2():
    # read_file("day5small.txt")
    read_file("day5.txt")

    all_id_ranges.sort(key=lambda tup: tup[0])
    do_stuff2()
    final_sum_2 = count_ranges()
    # display_list(all_id_ranges)
    print("-----")
    print(final_sum_2)


if __name__ == "__main__":
    day5_part2()
