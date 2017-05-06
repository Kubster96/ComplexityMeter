import numpy
import timeit
import matplotlib.pyplot as plt
from random import randint
import tkinter
import logging
from argparse import ArgumentParser
import math
# Loads module of the class and the class



def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


eny = [25, 50, 75, 100, 125, 150, 175, 200, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]
times = []
something = []
something2 = []
something3 = []
array = []

# TO DO tutaj bedzie mierzenie czasów


# TO DO tutaj bedzie obliczanie wspolczynnikow

def approximate(a, b, n):
    return numpy.polyfit(a, b, n)

# funkcje liczace srednie kwadratowe

def constant_function(x):
    return 1


def linear_function(x):
    return x


def square_function(x):
    return x**2


def cube_function(x):
    return x**3


def log_function(x):
    return math.log2(x)


def nlogn_function(x):
    return x*math.log2(x)


def ultimate_avg_error(function, factors, x, y):

    distances = []

    if len(factors) == 1:
        for i in range(0, len(x)):
            distances.append(abs((factors[0] * function(x[i])) - y[i]))

    else:
        for i in range(0, len(x)):
            distances.append(abs((factors[0] * function(x[i]) + factors[1]) - y[i]))
    return numpy.average(distances)


def perform(instance):

    for n in range(0, len(eny)):
        instance.init(n)
        timer = timeit.Timer(instance.function)
        t = timer.timeit(number=100)
        times.append(t)
        logging.debug("Time no. " + str(n) + " is " + str(t))

# Tutej niech sie zaczyna main tak jakby

logging.basicConfig(filename="logs.txt", level=logging.DEBUG)
logging.info("Start logging")

# Parser

parser = ArgumentParser()
parser.add_argument('class_module_name', help='Path to the class (something.something2.something3.className)'
                                              ' class must inherit from template class', type=str)

args = parser.parse_args()
my_class = my_import(args.class_module_name)
my_object = my_class()


print(args.class_module_name)


# liczenie wsplczynikow funkcji
perform(my_object)

constant = approximate(eny, times, 0)
logging.debug("Calculated linear approximation")
linear = approximate(eny, times, 1)
logging.debug("Calculated linear approximation")
square = approximate(numpy.power(eny, 2), times, 1)
logging.debug("Calculated square approximation")
cube = approximate(numpy.power(eny, 3), times, 1)
logging.debug("Calculated cube approximation")
logarithmic = approximate(numpy.log2(eny), times, 1)
logging.debug("Calculated logarithmic approximation")
n_logarithmic = approximate(eny*numpy.log2(eny), times, 1)
logging.debug("Calculated n_logarithmic approximation")

# for i in range(0, len(eny)):
#     something.append((square[0] * eny[i] ** 2 + square[1]))
#     something2.append((cube[0] * eny[i] ** 3 + cube[1]))
#     something3.append(n_logarithmic[0]*eny[i]*numpy.log2(eny[i]) + n_logarithmic[1])
#
# print(eny, len(eny))
# print(something, len(something))
#
# plt.plot(eny, times, 'ro')
# plt.plot(eny, something)
# plt.plot(eny, something2)
# plt.plot(eny, something3)
# plt.show()

errors = []
complexity = ["O(K)", "O(N)", "O(N^2)", "O(N^3)", "O(log(N))", "O(Nlog(N))"]

errors.append(ultimate_avg_error(constant_function, constant, eny, times))
errors.append(ultimate_avg_error(linear_function, linear, eny, times))
errors.append(ultimate_avg_error(square_function, square, eny, times))
errors.append(ultimate_avg_error(cube_function, cube, eny, times))
errors.append(ultimate_avg_error(log_function, logarithmic, eny, times))
errors.append(ultimate_avg_error(nlogn_function, n_logarithmic, eny, times))

logging.debug("Errors: " + str(errors))

print(errors)
print(complexity[errors.index(min(errors))])

logging.debug("Finished")
