# PART 1
def game_of_cups(starting_sequence,num_of_moves,min_cup=None,max_cup=None):
    # create a "linked list" dict
    cups = {
        starting_sequence[i] : starting_sequence[i+1]
        for i in range(len(starting_sequence)-1)
    }
    cups[starting_sequence[-1]] = starting_sequence[0]
    #
    current_cup = starting_sequence[0]
    max_cup = max_cup or max(starting_sequence)
    min_cup = min_cup or min(starting_sequence)

    for _ in range(num_of_moves):
        # cups to move are 3 ones after the current
        cups_to_move = (
            first := cups[current_cup],
            second := cups[first],
            third := cups[second]
        )
        # selects next current cup
        next_current_cup = cups[third]
        # destination is 1 less than current
        # if it's in the next 3 cups, it's 1 less than that, etc.
        # if it gets less than min, it loops back to max
        destination = current_cup - 1
        while destination in cups_to_move or destination<min_cup:
            destination -= 1

            if destination<min_cup:
                destination = max_cup

        # moves 3 cups after destination
        # by relinking destination to 1st cup
        # & third cup to cup after destination
        cup_after_destination = cups[destination]
        cups[destination] = first
        cups[third] = cup_after_destination

        # relinks current cup to next current cup
        cups[current_cup] = next_current_cup

        current_cup = next_current_cup

    return cups

def collect_result(cups_dict):
    output_string = ""

    next_cup = cups_dict[1]
    while next_cup!=1:
        output_string += str(next_cup)
        next_cup = cups_dict[next_cup]

    return output_string

# PART 2
def hyper_game_of_cups(starting_sequence):
    min_cup = min(starting_sequence)
    max_cup = max(starting_sequence)
    filled_starting_sequence = starting_sequence + list(range(max_cup+1,1_000_000+1))

    return game_of_cups(filled_starting_sequence,10_000_000,min_cup,1_000_000)

def hyper_collect_result(cups_dict):
    first = cups_dict[1]
    second = cups_dict[first]

    return first * second
