from random import randint

print('gets called')

input_list = [(randint(1, 123456789), randint(1, 123456789)) for _ in range(10_000)]
