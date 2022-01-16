from ticket_parser import *

# part 1
with open("tests/test_input_1.txt") as f:
    rules, your_ticket, nearby_tickets = parse_tickets(f)

invalid_values = find_invalid_values(rules,nearby_tickets)
assert invalid_values==[4, 55, 12]
assert sum(invalid_values)==71

valid_tickets = sieve_out_invalid_tickets(rules,nearby_tickets)
assert valid_tickets==[[7, 3, 47]]

# part 2
with open("tests/test_input_2.txt") as f:
    rules, your_ticket, nearby_tickets = parse_tickets(f)

valid_tickets = sieve_out_invalid_tickets(rules,nearby_tickets)
assert valid_tickets==[[3,9,18],[15,1,5],[5,14,9]]

all_tickets = [your_ticket] + valid_tickets
tickets_with_fields = translate_tickets_to_excluded_fields(rules,all_tickets)

fields = find_fields(rules,tickets_with_fields)
assert fields==["row", "class", "seat"]
