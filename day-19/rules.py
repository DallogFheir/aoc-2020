import re

class OrList(list):
    pass

def parse_input(fh):
    # parse rules
    rules_dict = {}

    for line in fh:
        if not re.match(r"\d",line):
            break
        
        index, rule = line.split(":")

        rule = rule.strip()
        # if rule contains |s, split on them and then split subrules by space
        if "|" in rule:
            subrules = rule.split("|")

            for i, subrule in enumerate(subrules):
                subrules[i] = OrList(int(r) for r in subrule.strip().split(" "))

            rule = subrules
        # if rule is "<letter>", remove ""
        elif re.match(r"\"[a-z]\"",rule):
            rule = rule.replace("\"","")
        # else split on spaces
        else:
            rule = [int(r) for r in rule.split(" ")]

        rules_dict[int(index)] = rule

    # parse messages
    messages = [line.strip() for line in fh.readlines()]

    return rules_dict, messages

def create_regex_str(rules,base_ind=0):
    base = rules[base_ind]

    rules_lst = _recursively_replace_rules(rules,base)
    regex_str = _recursively_join_into_regex(rules_lst)

    return regex_str

def _recursively_replace_rules(rules,rule):
    if isinstance(rule,str):
        return rule

    for i, el in enumerate(rule):
        if isinstance(el,str):
            rule[i] = el
        elif isinstance(el,int):
            rule[i] = _recursively_replace_rules(rules,rules[el])
        elif isinstance(el,list):
            rule[i] = _recursively_replace_rules(rules,el)

    return rule

def _recursively_join_into_regex(rules_lst):
    if isinstance(rules_lst,str):
        return rules_lst

    if all(isinstance(el,OrList) for el in rules_lst):
        joined = "|".join(f"({_recursively_join_into_regex(rule)})" for rule in rules_lst)

        return f'({joined})'
    
    return "".join(f"({(_recursively_join_into_regex(rule))})" for rule in rules_lst)
