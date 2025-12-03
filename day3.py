from itertools import combinations

all_voltages = list()
all_voltages_strings = list()
max_voltages = list()

def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            all_voltages.append(list(next_line.strip()))

def read_file2(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            all_voltages_strings.append(next_line.strip())

def do_stuff(voltage_group):
    # all_possible_max_voltages_for_group = set()
    # for i in range(len(voltage_group)-1):
    #     for j in range(i+1, len(voltage_group)):
    #         if voltage_group[i]+voltage_group[j] == "99":
    #             max_voltages.append(99)
    #             return
    #         all_possible_max_voltages_for_group.add(int(voltage_group[i]+voltage_group[j]))
    # max_voltages.append(max(all_possible_max_voltages_for_group))
    max_voltages.append(max([int(''.join(x)) for x in combinations(voltage_group, 2)]))

def do_stuff2(voltage_group):
    my_max = 0
    for comb in combinations(voltage_group, 12):
        if int(''.join(comb)) > my_max:
            my_max = int(''.join(comb))
    max_voltages.append(my_max)

def trim_voltage(voltage_group): # not used after all
    voltage_group_list = list(voltage_group)
    done = False
    while not done:
        min_voltage = min([int(x) for x in voltage_group_list])
        #can i remove all of them
        how_many_occurrences = voltage_group_list.count(str(min_voltage))
        if len(voltage_group_list) - how_many_occurrences >=12:
            #remove all of them
            temp_list = [x for x in voltage_group_list if x!=str(min_voltage)]
            voltage_group_list = temp_list.copy()
            print(voltage_group_list)
        else:
            #remove all from the beginning
            done_small = False
            while not done_small:
                lets_break = False
                element = voltage_group_list[0]
                while int(element) == min_voltage and len(voltage_group_list) > 12:
                    voltage_group_list.remove(element)
                    element = voltage_group_list[0]
                    print(voltage_group_list)
                # okay but is there a better number?
                for y in voltage_group_list:
                    if int(y) > int(element) and voltage_group_list.index(y) < len(voltage_group_list)-12:
                        voltage_group_list = voltage_group_list[voltage_group_list.index(y):]
                        print(voltage_group_list)
                        lets_break = True
                        break
                if lets_break:
                    continue
                done_small = True
            done = True
    print(voltage_group_list)
    return ''.join(voltage_group_list)

def trim_between(voltage_group):
    voltage_group_list = list(voltage_group)
    if len(voltage_group_list) == 12:
        return voltage_group
    done = False
    best_voltage = max([int(x) for x in voltage_group_list])
    index = 0
    while not done:
        while index < len(voltage_group_list):
            if int(voltage_group_list[index]) == best_voltage:
                index += 1
                continue
            broke = False
            for i in range(index + 1, len(voltage_group_list) - max([11-index, 0])):
                if int(voltage_group_list[index]) < int(voltage_group_list[i]):
                    del voltage_group_list[index]
                    # print(voltage_group_list)
                    broke = True
                    break
            if broke:
                continue
            index += 1
        done = True
    print(voltage_group_list)
    return ''.join(voltage_group_list)
    # would not work for every possible input :( e.g. input is 100x the same number


def day3_part1():
    # read_file("day3small.txt")
    read_file("day3.txt")
    for vg in all_voltages:
        do_stuff(vg)
    final_sum_1 = sum(max_voltages)
    # display_list(all_voltages)
    print("-----")
    # display_list(max_voltages)
    print("-----")

    print(final_sum_1)

def day3_part2():
    # read_file2("day3small.txt")
    read_file2("day3.txt")
    for vg in all_voltages_strings:
        # first_trim = trim_voltage(vg)
        do_stuff2(trim_between(vg))
        print(f"one done: {len(max_voltages)}")
    final_sum_2 = sum(max_voltages)
    # display_list(all_voltages)
    print("-----")
    # display_list(max_voltages)
    print("-----")

    print(final_sum_2)


if __name__ == "__main__":
    day3_part2()
