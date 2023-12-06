

def file_reader(filename):
    # This function reads a text file that contains string lines and returns those lines in a list
    fr = open(filename, "r")
    lines = (fr.read()).splitlines()
    return lines

def extract_number_string(random_string, index):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    found_index=None

    for word in words:
        found_index = random_string[index:index+len(word)].find(word)
        if found_index != -1:
            number_as_string = str(words.index(word))
            return number_as_string, found_index+len(word)

    if found_index == -1:
        return "", found_index

def first_and_last_only(val):
    # Reduce the number string to just first and last digits (or duplicate first)
    val = val[0] + val[len(val) - 1]
    return val

def sum_number_string_vals(string_vals):
    # This function converts all number string values in a
    # list to integers, sums them up, and prints the sum.
    big_sum=0
    for number in string_vals:
        big_sum = big_sum + int(number)
    return big_sum


def main():
    filename = "day1input.txt"
    example_filename = "day1part2inputexample.txt"
    lines = file_reader(filename)

    # Initialize numbers list and other vars
    vals = [""] * len(lines)

    x = 0
    v = 0

    # Loop through every line, then every character on every line and
    # either extract a number or a number word
    for line in lines:
        print(line)
        chars = [x for x in line]
        i=0
        while i < len(chars):
            if chars[i].isalpha():
                number_string_and_index = extract_number_string(line, i)

                if number_string_and_index[1] != -1:
                    if vals[v] == "":
                        vals[v]= number_string_and_index[0]
                    else:
                        vals[v] = vals[v] + number_string_and_index[0]

                    i = i + number_string_and_index[1]

                else:
                    i=i+1

            else:
                if vals[v] == "":
                    vals[v] = chars[i]
                else:
                    vals[v] = vals[v] + chars[i]
                i=i+1
        print(vals[v])
        vals[v]=first_and_last_only(vals[v])
        print(vals[v])
        v=v+1

    #vals = first_and_last_only(vals)

    answer = sum_number_string_vals(vals)
    print("The sum is " + str(answer))

# Required python variable for the silly thing to run
if __name__=="__main__":
    main()
