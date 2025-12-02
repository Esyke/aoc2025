
all_ids = list()
bad_ids = list()

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            all_id_lines = next_line.split(",")
    for id_lines in all_id_lines:
        all_ids.append((int(id_lines.split("-")[0]), int(id_lines.split("-")[1])))

def do_stuff(range_start: int, range_end: int):
    for x in range(range_start, range_end+1):
        if len(str(x))%2 == 1:
            continue
        elif str(x)[0:int(len(str(x))/2)] == str(x)[int(len(str(x))/2):len(str(x)):]:
            bad_ids.append(x)

def do_stuff2(range_start: int, range_end: int):
    for x in range(range_start, range_end+1):
        bad_ids.append(find_pattern(str(x)))

def find_pattern(my_id: str):
    for possible_pattern_base_number in range(1, int(len(my_id) / 2 + 1)):
        if len(my_id)%possible_pattern_base_number != 0:
            continue
        my_ids = list()
        for id_seq_number in range(int(len(my_id) / possible_pattern_base_number)):
            my_ids.append(my_id[id_seq_number * possible_pattern_base_number:(id_seq_number + 1) * possible_pattern_base_number])
        if len(set(my_ids)) == 1:
            return int(my_id)

    return 0
def day2_part1():
    # read_file("day2small.txt")
    read_file("day2.txt")

    for x in range(len(all_ids)):
        do_stuff(all_ids[x][0], all_ids[x][1])
    final_sum_1 = sum(bad_ids)
    display_list(all_ids)
    print("-----")
    display_list(bad_ids)
    print("-----")

    print(final_sum_1)

def day2_part2():
    # read_file("day2small.txt")
    read_file("day2.txt")

    for x in range(len(all_ids)):
        do_stuff2(all_ids[x][0], all_ids[x][1])
    final_sum_2 = sum(bad_ids)
    # display_list(all_ids)
    # print("-----")
    # display_list(bad_ids)
    print("-----")

    print(final_sum_2)



if __name__ == "__main__":
    day2_part2()
