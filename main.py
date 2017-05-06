import numpy
import timeit
import matplotlib.pyplot as plt
from random import randint
import tkinter
import logging
from argparse import ArgumentParser

# Loads module of the class and the class

def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


eny = [25, 50, 75, 100, 125, 150, 175, 200, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 1000]
times = []
something = []
something2 = []
array = []

# TO DO tutaj bedzie mierzenie czasów


# TO DO tutaj bedzie obliczanie wspolczynnikow

def approximate(a, b, n):
    return numpy.polyfit(a, b, n)

# funkcje liczace srednie kwadratowe


def square_root_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0]*numpy.sqrt(x[i]) + factor[1]) - y[i]))
    return numpy.average(distances)


def constant_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs(factor[0] - y[i]))
    return numpy.average(distances)


def linear_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0] * x[i] + factor[1]) - y[i]))
    return numpy.average(distances)


def square_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0] * x[i] ** 2 + factor[1] * x[i] + factor[2]) - y[i]))
    return numpy.average(distances)


def cube_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0] * x[i] ** 3 + factor[1] * x[i] ** 2 + factor[2] * x[i] + factor[3]) - y[i]))
    return numpy.average(distances)


def logarithm_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0]*numpy.log2(x[i]) + factor[1]) - y[i]))
    return numpy.average(distances)


def n_logarithm_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0]*x[i]*numpy.log2(x[i])) - y[i]))
    return numpy.average(distances)


def perform(instance):

    for n in range(0, len(eny)):
        instance.init(n)
        timer = timeit.Timer(instance.function)
        t = timer.timeit(number=1)
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
square = approximate(eny, times, 2)
logging.debug("Calculated square approximation")
cube = approximate(eny, times, 3)
logging.debug("Calculated cube approximation")
logarithmic = approximate(numpy.log2(eny), times, 1)
logging.debug("Calculated logarithmic approximation")
n_logarithmic = approximate(eny*numpy.log2(eny), times, 1)
logging.debug("Calculated n_logarithmic approximation")


print(constant)
print(linear)
print(square)
print(cube)
print(logarithmic)
print(n_logarithmic)


# for i in range(0, len(eny)):
#     something.append((square[0] * eny[i] ** 2 + square[1] * eny[i] + square[2]))
#     something2.append((cube[0] * eny[i] ** 3 + cube[1] * eny[i] ** 2 + cube[2] * eny[i] + cube[3]))
#
# print(eny, len(eny))
# print(something, len(something))
#
# plt.plot(eny, times, 'ro')
# plt.plot(eny, something)
# plt.plot(eny, something2)
# plt.show()

errors = []
complexity = ["O(K)", "O(N)", "O(N^2)", "O(N^3)", "O(log(N))", "O(Nlog(N))"]

errors.append(constant_avg_error(constant, eny, times))
errors.append(linear_avg_error(linear, eny, times))
errors.append(square_avg_error(square, eny, times))
errors.append(cube_avg_error(cube, eny, times))
errors.append(logarithm_avg_error(logarithmic, eny, times))
errors.append(n_logarithm_avg_error(n_logarithmic, eny, times))

print(errors)
print(complexity[errors.index(min(errors))])

logging.debug("Finished")
