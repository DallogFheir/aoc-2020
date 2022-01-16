import re
from rules import create_regex_str, parse_input

with open("test_input/test_input_1.txt") as f:
    rules_1, _ = parse_input(f)
with open("test_input/test_input_2.txt") as f:
    rules_2, messages_2 = parse_input(f)
with open("test_input/test_input_3.txt") as f:
    rules_3, messages_3 = parse_input(f)

# test 1
regex_1 = re.compile(create_regex_str(rules_1))

assert re.fullmatch(regex_1,"aab") is not None
assert re.fullmatch(regex_1,"aba") is not None

# test 2
regex_2 = re.compile(create_regex_str(rules_2))
matches = ["aaaabb", "aaabab", "abbabb", "abbbab", "aabaab", "aabbbb", "abaaab", "ababbb"]
not_matches = ["bababa", "aaabbb", "aaaabbb"]

for match in matches:
    assert re.fullmatch(regex_2, match) is not None

for not_match in not_matches:
    assert re.fullmatch(regex_2, not_match) is None

assert sum(re.fullmatch(regex_2, msg) is not None for msg in messages_2)==2

# test 3
regex_3 = re.compile(create_regex_str(rules_3))
matches = ["bbabbbbaabaabba", "ababaaaaaabaaab", "ababaaaaabbbaba"]

for match in matches:
    assert re.fullmatch(regex_3, match) is not None

assert sum(re.fullmatch(regex_3, msg) is not None for msg in messages_3)==3

# part 2
regex_42_str = create_regex_str(rules_3,42)
regex_31_str = create_regex_str(rules_3,31)
regex = re.compile(f"{regex_42_str}+{regex_31_str}+")

matches = [
    "bbabbbbaabaabba",
    "babbbbaabbbbbabbbbbbaabaaabaaa",
    "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
    "bbbbbbbaaaabbbbaaabbabaaa",
    "bbbababbbbaaaaaaaabbababaaababaabab",
    "ababaaaaaabaaab",
    "ababaaaaabbbaba",
    "baabbaaaabbaaaababbaababb",
    "abbbbabbbbaaaababbbbbbaaaababb",
    "aaaaabbaabaaaaababaa",
    "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
    "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"
]

for match in matches:
    assert re.fullmatch(regex, match) is not None

assert sum(re.fullmatch(regex, msg) is not None for msg in messages_3)==12
