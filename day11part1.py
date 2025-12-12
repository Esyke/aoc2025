path_count_by_id = dict()
output_by_id = dict()
relevant_devices = set()
you = 'you'
out = 'out'



def display_list(my_list):
    print("--------------------------------------")
    for line in my_list:
        print(line)

def read_file(file_name):
    with open(f"inputs/{file_name}", "r") as f:
        for next_line in f:
            output_by_id[next_line.split(':')[0]] = next_line.split(':')[1].strip().split(' ')


def collect_relevant_devices():
    newly_relevant_devices = output_by_id[you].copy()
    relevant_devices.add(you)
    while len(newly_relevant_devices) > 0:
        relevant_devices.add(newly_relevant_devices[0])
        if newly_relevant_devices[0] != out:
            newly_relevant_devices.extend(output_by_id[newly_relevant_devices[0]])
        newly_relevant_devices = [d for d in newly_relevant_devices if d != newly_relevant_devices[0]]

def trim_device_list():
    trimmed_dict = dict()
    for device, output_devices in output_by_id.items():
        if device not in relevant_devices:
            continue
        else:
            path_count_by_id[device] = 0
            trimmed_dict[device] = [x for x in output_devices if x in relevant_devices]
    return trimmed_dict

def count_backwards(trimmed_dict):
    work_list = relevant_devices.copy()
    path_count_by_id[out] = 1
    work_list.remove(out)
    while len(work_list) > 0:
        for item in work_list:
            # if all your children have a number
            if all([path_count_by_id[x] > 0 for x in trimmed_dict[item]]):
                path_count_by_id[item] = sum([path_count_by_id[x] for x in trimmed_dict[item]])
                work_list.remove(item)
                break

def day11_part1():
    # read_file("day11small.txt")
    read_file("day11.txt")
    # display_list(output_by_id.items())

    collect_relevant_devices()
    trimmed_output_by_id = trim_device_list()
    # display_list(trimmed_output_by_id.items())
    count_backwards(trimmed_output_by_id)
    # display_list(path_count_by_id.items())
    final_sum_1 = path_count_by_id[you]
    print("-----")

    print(final_sum_1)

if __name__ == "__main__":
    day11_part1()
