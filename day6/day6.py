
def main():

    # Time: 7 15 30
    # Distance: 9 40 200
    # race_time = [7, 15, 30]
    # best_distance = [9, 40, 200]
    #race_time = [71530]
    #best_distance = [940200]

    # Time: 54 81 70 88
    # Distance: 446 1292 1035 1007
    # race_time = [54, 81, 70, 88]
    # best_distance = [446, 1292, 1035, 1007]
    race_time = [54817088]
    best_distance = [446129210351007]


    i=0
    wins=[]
    final_product=1

    for time in race_time:
        number_of_wins = 0
        hold_time = 0
        while hold_time < time:
            if hold_time * (int(time) - hold_time) > best_distance[i]:
                number_of_wins = number_of_wins + 1
            hold_time = hold_time + 1
        print("For the Time=" + str(time) + " and Distance=" + str(best_distance[i]) + " there are " + str(number_of_wins) + " ways to win.")
        #wins.append(number_of_wins)
        i=i+1

    # Comment out for part 2
    # if len(wins) > 0:
    #     for win in wins:
    #         final_product = win * final_product
    #
    # print("Final product: " + str(final_product))


# Required python variable for the silly thing to run
if __name__ == "__main__":
    main()