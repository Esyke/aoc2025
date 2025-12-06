import re

numbers_regex = r"\s*(\d+).* "
operand_list = list()
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
                if len(solution_list) == 0:
                    solution_list = [int(z) for z in next_line.strip().split(' ') if z != '']
                else:
                    operand_list.append([int(x) for x in next_line.strip().split(' ') if x != ''])
            else:
                operator_list = [y for y in next_line.strip().split(' ') if y != '']


def do_stuff():
    for row_id in range(len(operand_list)):
        for col_id in range(len(operand_list[row_id])):
            if operator_list[col_id] == '+':
                solution_list[col_id] += operand_list[row_id][col_id]
            elif operator_list[col_id] == '*':
                solution_list[col_id] *= operand_list[row_id][col_id]
            else:
                print("why")


def day6_part1():
    # read_file("day6small.txt")
    read_file("day6.txt")
    do_stuff()
    final_sum_1 = sum(solution_list)
    # display_list(operand_list)
    print("-----")
    # display_list(operator_list)
    print("-----")
    # display_list(solution_list)
    print("-----")

    print(final_sum_1)




if __name__ == "__main__":
    day6_part1()
