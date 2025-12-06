import re

fresh_range_regex = r"(\d+)-(\d+)"
product_regex = r"(\d+)"
fresh_ids = set()
fresh_id_ranges = list()
all_sus_ids = list()
ids_dict = dict()


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if re.match(fresh_range_regex, next_line):
                match = re.match(fresh_range_regex, next_line)
                fresh_id_ranges.append((int(match.groups()[0]), int(match.groups()[1])+1))
            elif re.match(product_regex, next_line):
                match = re.match(product_regex, next_line)
                all_sus_ids.append(int(match.groups()[0]))

def do_stuff():
    fresh_count = 0
    for sus_id in all_sus_ids:
        for id_range in fresh_id_ranges:
            if id_range[0] <= sus_id <= id_range[1]:
                fresh_count += 1
                break
    return fresh_count


def day5_part1():
    # read_file("day5small.txt")
    read_file("day5.txt")

    final_sum_1 = do_stuff()
    # display_list(fresh_id_ranges)
    print("-----")

    print(final_sum_1)




if __name__ == "__main__":
    day5_part1()
