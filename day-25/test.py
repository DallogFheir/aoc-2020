from handshake import *

assert find_loop_size(5764801)==8
assert find_loop_size(17807724)==11

assert create_key(8,17807724)==14897079
assert create_key(11,5764801)==14897079
