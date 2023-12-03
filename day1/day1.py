
# Read the file input
fr = open("day1input.txt", "r")
#fr = open("day1inputexample.txt", "r")
lines = (fr.read()).splitlines()

# Initialize numbers list and other vars
vals=[None]*len(lines)

bigSum=0
i=0
x=0

# Loop through every line, then every character on every line and extract numbers
for line in lines:
    chars = [x for x in line]

    for char in chars:
        if not char.isalpha():
            if vals[i] == None:
                vals[i]=char
            else:
                vals[i]=vals[i]+char
    i+=1

# Fix all the values to be first and last digit (or duplicate the first)
j=0
for val in vals:
    if len(val) < 2:
        vals[j]=val[0]+val[0]
    if len(val) > 2:
        vals[j]=val[0]+val[len(val)-1]
    j+=1


# Sum up all of the numbers
for number in vals:
    bigSum = bigSum + int(number)
print(bigSum)


