import re

numbers_regex = r"\s*(\d+).* "
full_operand_list = list()
operator_list = list()
solution_list = list()


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    global operator_list
    global solution_list
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            if re.match(numbers_regex, next_line):
                full_operand_list.append(list(next_line[:-1]))
            else:
                operator_list = [y for y in next_line.strip().split(' ') if y != '']

def separate_problems_and_do_stuff():
    operator_list_index = 0
    for char_index in range(len(full_operand_list[0])):
        temp_list = [c[char_index] for c in full_operand_list]
        if all(x==' ' for x in temp_list):
            operator_list_index+=1
        else:
            assembled_number = int((''.join(temp_list)).strip())
            if len(solution_list)==operator_list_index:
                solution_list.append(assembled_number)
            else:
                if operator_list[operator_list_index] == '+':
                    solution_list[operator_list_index] += assembled_number
                elif operator_list[operator_list_index] == '*':
                    solution_list[operator_list_index] *= assembled_number
                else:
                    print("why")
    return


def day6_part2():
    # read_file("day6small.txt")
    read_file("day6.txt")
    separate_problems_and_do_stuff()
    final_sum_2 = sum(solution_list)
    # print(full_operand_list)
    print("-----")
    # print(operator_list)
    print("-----")
    # display_list(solution_list)
    print("-----")

    print(final_sum_2)




if __name__ == "__main__":
    day6_part2()
