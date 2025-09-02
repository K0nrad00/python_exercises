'''
Objective Create your own decorator function to measure the amount of seconds that a function takes to execute. Expected Output

1695050908.1985211
fast_function run speed: 0.33974480628967285s
slow_function run speed: 2.9590742588043213s

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator():
  pass

def fast_function():
  for i in range(1000000):
    i * i


def slow_function():
  for i in range(10000000):
    i * i
'''

import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def measure_time():
        start = current_time
        function()
        finish = time.time()
        print(f"run time of {function}: {finish - start}")
    return measure_time


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
