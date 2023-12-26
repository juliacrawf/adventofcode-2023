
def parse_steps(steps):
    i = 0
    labels = [""] * len(steps)
    operations = [""] * len(steps)
    focal_lengths = [""] * len(steps)

    for step in steps:
        if "-" in step:
            operations[i] = "-"
            labels[i] = step[0:step.find("-")]
        if "=" in step:
            operations[i]="="
            labels[i] = step[0:step.find("=")]
            focal_lengths[i] = step[step.find("=")+1:len(step)]
        i += 1
    return labels, operations, focal_lengths

def apply_hash(input_string):
    hash_value=0
    for char in input_string:
        hash_value = (hash_value + (ord(char))) * 17
        hash_value = hash_value % 256
    return hash_value

def get_hash_sum(list_hash_strings):
    sum=0
    for hash_string in list_hash_strings:
        hash_value = apply_hash(hash_string)
        sum=sum+hash_value
    return sum

def get_focusing_power(box, box_index, lens, lens_label, slot):
    focusing_power=0
    if lens_label in box:
        focal_length = int((lens)[lens.find(" ") + 1:lens.find("]")])
        focusing_power=(1+box_index)*(slot)*focal_length
    return focusing_power

def file_reader(filename):
    # This function reads a text file that contains a very long comma-separated string, returned in a list
    fr = open(filename, "r")
    hash_strings = (fr.read()).split(",")
    return hash_strings

def main():
    filename = "day15input.txt"
    #filename = "day15inputexample.txt"

    list_hash_strings = file_reader(filename)
    #list_hash_strings = ("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7").split(",")

    labels_operations_focals=parse_steps(list_hash_strings)
    boxes = [""] * 256

    i=0

    while i < len(labels_operations_focals[0]):
        box_index = apply_hash(labels_operations_focals[0][i])
        lens_start_string = "[" + labels_operations_focals[0][i] + " "
        lens_start_index = (boxes[box_index]).find(lens_start_string)

        if (labels_operations_focals[1][i] == "-") & (lens_start_index != -1):
            boxes[box_index]=boxes[box_index][0:lens_start_index] + boxes[box_index][lens_start_index+len(lens_start_string)+2:len(boxes[box_index])]

        if labels_operations_focals[1][i] == "=":
            new_lens = "[" + labels_operations_focals[0][i] + " " + labels_operations_focals[2][i] + "]"
            if lens_start_string in boxes[box_index]:
                boxes[box_index] = boxes[box_index][0:lens_start_index] + new_lens + boxes[box_index][lens_start_index + len(lens_start_string)+2:len(boxes[box_index])]
            else:
                boxes[box_index]=boxes[box_index]+new_lens
        i += 1

    sum_powers=0
    count=0

    while count < len(boxes):

        box = boxes[count]
        lenses = [x + "]" for x in box.split("]") if x]
        slot = 1
        for lens in lenses:

            lens_label = lens[1:lens.index(" ")+1]
            while slot < len(lenses)+1:
                if lens_label in lenses[slot-1]:
                    break
                slot += 1
            lens_power=get_focusing_power(box,count,lens,lens_label,slot)

            sum_powers = sum_powers+lens_power
        count += 1

    print(str(sum_powers))

# Required python variable for the silly thing to run
if __name__ == "__main__":
    main()