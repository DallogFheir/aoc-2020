import re
import numpy as np

def parse_tickets(fh):
    # parsing rules
    rule_pattern = re.compile(r"(.*?):(( (or )?\d+-\d+)+)")
    rules = {}
    for line in fh:
        line = line.strip()

        if line.startswith("your ticket:"):
            break

        match = rule_pattern.match(line)
        if match is not None:
            rule, ranges_str, *_ = match.groups()

            ranges = [
                range(
                    int(range_str.split("-")[0]),
                    int(range_str.split("-")[1])+1
                    )
                for range_str in ranges_str.strip().split(" or ")
            ]

            rules[rule] = ranges

    # parsing your ticket
    your_ticket = [int(value) for value in fh.readline().strip().split(",")]

    # get to nearby tickets
    for line in fh:
        if line.startswith("nearby tickets:"):
            break

    # parsing nearby tickets
    nearby_tickets = []
    for line in fh:
        ticket = [int(value) for value in line.strip().split(",")]

        nearby_tickets.append(ticket)

    return rules, your_ticket, nearby_tickets

def find_invalid_values(rules,tickets):
    invalid_values = []

    for ticket in tickets:
        for value in ticket:
            if not check_if_all_valid(rules,value):
                invalid_values.append(value)

    return invalid_values

def check_if_all_valid(rules,value):
    if all(
        not check_if_valid(rule,value)
        for rule in rules.values()
    ):
        return False

    return True

def check_if_valid(rule,value):
    for rule_range in rule:
        if value in rule_range:
            return True

    return False

def sieve_out_invalid_tickets(rules,tickets):
    valid_tickets = []

    for ticket in tickets:
        if all(check_if_all_valid(rules,value) for value in ticket):
            valid_tickets.append(ticket)

    return valid_tickets

def translate_tickets_to_excluded_fields(rules,tickets):
    all_tickets = []

    for ticket in tickets:
        ticket_fields = []

        for value in ticket:
            excluded_fields = set(
                field 
                for field, rule in rules.items()
                if not check_if_valid(rule,value)
            )

            ticket_fields.append(excluded_fields)

        all_tickets.append(ticket_fields)

    return all_tickets

def find_fields(rules,tickets_with_fields):
    rules_set = set(rules.keys())
    fields = [None] * len(rules)
    tickets = np.array(tickets_with_fields)

    while fields.count(None)!=0:
        for i in range(len(tickets[0])):
            column_set = set()

            # for each column sum all sets
            for value_set in tickets[:,i]:
                column_set.update(value_set)

            # get difference between all fields and all column excluded sets
            set_diff = rules_set - column_set
            if len(set_diff)==1:
                field = tuple(set_diff)[0]
                rules_set.remove(field)
                fields[i] = field

    return fields
