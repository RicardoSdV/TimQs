from timeit import Timer

from nineFac.makeRndInputs import input_list
from nineFac.ric import ric_seq
from nineFac.tim import tim_seq


def callRic():
    for args in input_list:
        ric_seq(*args)


def callTim():
    for args in input_list:
        tim_seq(*args)


def time_all():
    num_runs = 100

    print('Ric time:', Timer(callRic).timeit(number=num_runs))
    print('Tim time:', Timer(callTim).timeit(number=num_runs))

time_all()
