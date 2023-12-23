
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
        i = i+1
    return labels, operations, focal_lengths

def apply_hash(input_string):
    hash_value=0
    for char in input_string:
        hash_value = (hash_value + (int(ord(char)))) * 17
        hash_value = hash_value % 256
    return hash_value

def get_hash_sum(list_hash_strings):
    sum=0
    for hash_string in list_hash_strings:
        hash_value = apply_hash(hash_string)
        sum=sum+hash_value
    return sum

def get_focusing_power(box, box_index, lens, lens_label, slot):
    print("box " + str(box_index) + " " + box)
    focusing_power=0
    if lens_label in box:
        focal_length = int((lens)[lens.find(" ") + 1:lens.find("]")])
        focusing_power=(1+box_index)*(slot)*focal_length
    return focusing_power

def file_reader(filename):
    # This function reads a text file that contains a very long comma-separated strings, returned in a list
    fr = open(filename, "r")
    hash_strings = (fr.read()).split(",")
    return hash_strings

def main():
    filename = "day15input.txt"

    list_hash_strings = file_reader(filename)
    #list_hash_strings = ("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7").split(",")
    #list_hash_strings=("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7,gzktrh=3,cg=4,rh=6,rh-,gzktrh=1,xzh=2,rh-").split(",")

    labels_operations_focals=parse_steps(list_hash_strings)
    boxes = [""] * 256

    i=0
    print("-----FILL BOXES-----")
    while i < len(labels_operations_focals[0]):
        print("After: " + labels_operations_focals[0][i]+labels_operations_focals[1][i]+labels_operations_focals[2][i])
        box_index = apply_hash(labels_operations_focals[0][i])
        print("(before) Box " + str(box_index) + boxes[box_index])
        lens_start_string = "[" + labels_operations_focals[0][i] + " "
        lens_start_index = (boxes[box_index]).find(lens_start_string)
        if lens_start_index == -1:
            lens_start_index=0

        if labels_operations_focals[1][i] == "-":
            if ("[" + labels_operations_focals[0][i] + " ") in boxes[box_index]:
                boxes[box_index]=boxes[box_index][0:lens_start_index] + boxes[box_index][lens_start_index+len(lens_start_string)+2:len(boxes[box_index])]

        if labels_operations_focals[1][i] == "=":
            new_lens = "[" + labels_operations_focals[0][i] + " " + labels_operations_focals[2][i] + "]"
            if ("["+labels_operations_focals[0][i] + " ") in boxes[box_index]:
                boxes[box_index] = boxes[box_index][0:lens_start_index] + new_lens + boxes[box_index][lens_start_index + len(lens_start_string)+2:len(boxes[box_index])]
            else:
                boxes[box_index]=boxes[box_index]+new_lens
        print("(after) Box " + str(box_index) + boxes[box_index])
        i = i+1

    sum_powers=0
    box_index=0

    print("-----GET BOX POWERS-----")
    while box_index < len(boxes):
        box = boxes[box_index]
        lenses = [x + "]" for x in box.split("]") if x]
        slot = 1
        for lens in lenses:
            lens_label = lens[1:lens.index(" ")]
            while slot < len(lenses)+1:
                if lens_label in lenses[slot-1]:
                    break
                slot = slot + 1
            lens_power=get_focusing_power(box,box_index,lens,lens_label,slot)
            print("lens power for " + lens_label + " = " + str(lens_power))
            sum_powers=sum_powers+lens_power
            print("current sum powers = " + str(sum_powers))
        box_index=box_index+1

    print(str(sum_powers))

# Required python variable for the silly thing to run
if __name__ == "__main__":
    main()