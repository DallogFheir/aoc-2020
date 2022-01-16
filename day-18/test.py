from tree import Tree

# standard - left to right
assert Tree("1 + 2 * 3 + 4 * 5 + 6",mode="standard").eval()==71
assert Tree("1 + (2 * 3) + (4 * (5 + 6))",mode="standard").eval()==51
assert Tree("2 * 3 + (4 * 5)",mode="standard").eval()==26
assert Tree("5 + (8 * 3 + 9 + 3 * 4 * 3)",mode="standard").eval()==437
assert Tree("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",mode="standard").eval()==12240
assert Tree("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",mode="standard").eval()==13632

# advanced - + before *
assert Tree("1 + 2 * 3 + 4 * 5 + 6",mode="advanced").eval()==231
assert Tree("1 + (2 * 3) + (4 * (5 + 6))",mode="advanced").eval()==51
assert Tree("2 * 3 + (4 * 5)",mode="advanced").eval()==46
assert Tree("5 + (8 * 3 + 9 + 3 * 4 * 3)",mode="advanced").eval()==1445
assert Tree("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",mode="advanced").eval()==669060
assert Tree("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",mode="advanced").eval()==23340
