
def file_reader(filename):
    # This function reads a text file that contains a very long comma-separated strings, returned in a list
    fr = open(filename, "r")
    hash_strings = (fr.read()).split(",")
    return hash_strings

def main():
    filename = "day15input.txt"

    list_hash_strings = file_reader(filename)
    #list_hash_strings=("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7").split(",")


    sum=0

    for hash_string in list_hash_strings:

        hash_value = 0

        for char in hash_string:
            hash_value=(hash_value+(int(ord(char))))*17
            hash_value = hash_value % 256

        print(hash_value)
        sum=sum+hash_value

    print("The sum of the hash values is " + str(sum))




# Required python variable for the silly thing to run
if __name__ == "__main__":
    main()