def create_key(loop_size,subject_number):
    loop = encryption_loop(subject_number)

    for _ in range(loop_size):
        value = next(loop)

    return value

def encryption_loop(subject_number):
    value = 1
    while True:
        value *= subject_number
        value %= 20201227

        yield value

def find_loop_size(key):
    loop = encryption_loop(7)
    secret_loop_size = 1
    while True:
        value = next(loop)

        if value==key:
            return secret_loop_size
        
        secret_loop_size += 1
