import itertools
import math

all_boxes = list()
circuit_dict = dict()
pairs = list()
distances = list()

class JunctionBox:
    def __init__(self, coo, c):
        self.x = int(coo[0])
        self.y = int(coo[1])
        self.z = int(coo[2])
        self.circuit_id = c
        self.happy = False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    @staticmethod
    def distance_between_junction_boxes(jb1, jb2):
        return math.pow((math.pow(jb1.x-jb2.x, 2) + math.pow(jb1.y-jb2.y, 2) + math.pow(jb1.z-jb2.z, 2)), 0.5)

    def print(self):
        print(f"[{self.x},{self.y},{self.z}] on circuit [{self.circuit_id}]")

    def move_to_circuit_from_circuit(self, from_c, to_c):
        if self.circuit_id == from_c:
            self.circuit_id = to_c
            circuit_dict[from_c]-=1
            circuit_dict[to_c]+=1
            return True
        return False

def find_next_n_distances(length=1000):
    max_distance = 0.0
    for pair in itertools.combinations(all_boxes, 2):
        if len(pairs)<length:
            pairs.append(pair)
            distance = JunctionBox.distance_between_junction_boxes(pair[0], pair[1])
            distances.append(distance)
            if max_distance<distance:
                max_distance = distance
        else:
            distance = JunctionBox.distance_between_junction_boxes(pair[0], pair[1])
            if max_distance > distance:
                index = distances.index(max_distance)
                del pairs[index]
                del distances[index]
                pairs.append(pair)
                distances.append(distance)
                max_distance = max(distances)

def connect_boxes():
    for pair in pairs:
        if pair[0].circuit_id == pair[1].circuit_id:
            continue
        c0 = pair[0].circuit_id
        c1 = pair[1].circuit_id
        for box in all_boxes:
            box.move_to_circuit_from_circuit(c0, c1)



def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        if isinstance(line, JunctionBox):
            line.print()
        else:
            print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        i = 0
        for next_line in f:
            all_boxes.append(JunctionBox(next_line.split(','), i))
            circuit_dict[i] = 1
            i += 1


def day8_part1():
    # read_file("day8small.txt")
    read_file("day8.txt")
    find_next_n_distances()
    # display_list(distances)
    connect_boxes()
    circuit_dict_list = sorted([v for v in circuit_dict.values()], reverse=True)
    final_sum_1 = circuit_dict_list[0]*circuit_dict_list[1]*circuit_dict_list[2]
    # display_list(all_boxes)
    print("-----")

    print(final_sum_1)


if __name__ == "__main__":
    day8_part1()
