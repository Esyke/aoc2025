
diagram = list()
tachyon_beam = "|"
tachyon_beam_start = "S"
empty_space = "."
splitter = "^"


def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            diagram.append(list(next_line.strip()))

def fill_in_diagram_with_tachyon_beams():
    times_split = 0
    diagram[0][diagram[0].index(tachyon_beam_start)] = tachyon_beam
    for i in range(1, len(diagram)):
        for j in range(len(diagram[i])):
            split = False
            if diagram[i-1][j] == tachyon_beam:
                if diagram[i][j] == empty_space:
                    diagram[i][j] = tachyon_beam
                elif diagram[i][j] == splitter:
                    if diagram[i][j-1] == empty_space:
                        diagram[i][j-1] = tachyon_beam
                        split = True
                    if diagram[i][j+1] == empty_space:
                        diagram[i][j+1] = tachyon_beam
                        split = True
            times_split += int(split)
    return times_split

def count_all_paths():
    diagram[len(diagram)-1] = [x if x!=tachyon_beam else '1' for x in diagram[len(diagram)-1] ]
    for i in range(len(diagram)-2, -1, -1):
        for j in range(len(diagram[i])):
            if diagram[i][j] == tachyon_beam:
                if diagram[i+1][j].isdigit():
                    diagram[i][j] = diagram[i+1][j]
                if diagram[i+1][j] == splitter:
                    diagram[i][j] = str(int(diagram[i+1][j-1]) + int(diagram[i+1][j+1]))

    return int([x for x in diagram[0] if x.isdigit()][0])

def day7_part1():
    # read_file("day7small.txt")
    read_file("day7.txt")

    final_sum_1 = fill_in_diagram_with_tachyon_beams()
    # display_list(diagram)
    print("-----")

    print(final_sum_1)

def day7_part2():
    # read_file("day7small.txt")
    read_file("day7.txt")

    fill_in_diagram_with_tachyon_beams()
    final_sum_2 = count_all_paths()
    # display_list(diagram)
    print("-----")
    print(final_sum_2)

if __name__ == "__main__":
    day7_part2()
