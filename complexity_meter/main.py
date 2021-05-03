import numpy
import timeit
import matplotlib.pyplot as plt
import logging
from argparse import ArgumentParser
import time
# Loads module of the class and the class


class ClassNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


eny = [25, 50, 75, 100, 125, 150, 175, 200, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]
coefficients = []
times = []
something = []
something2 = []
something3 = []
errors = []
complexity = ["O(K)",
              "O(N)",
              "O(N^2)",
              "O(N^3)",
              "O(log(N))",
              "O(Nlog(N))"]

functions = ["a",
             "a*x + b",
             "a*x^2 + b",
             "a*x^3 + b",
             "a*logx + b",
             "a*xlogx + b"]

rev_functions = ["x = a ",
                 "x = (y - b)/a",
                 "x = (y - b)/a)^(1/2)",
                 "x = (y - b)/a ^(1/3)",
                 "2^((y - b)/a)",
                 "reverse does not exist"]


def my_import(name):
    try:
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)

    except(ImportError, AttributeError):
        raise ClassNotFoundException("Class not found")

    return mod


# approximate function and all functions with avg error

def approximate(a, b, n):
    return numpy.polyfit(a, b, n)


def constant_function(x):
    return 1


def linear_function(x):
    return x


def square_function(x):
    return x**2


def cube_function(x):
    return x**3


def log_function(x):
    return numpy.log2(x)


def nlogn_function(x):
    return x*numpy.log2(x)


def ultimate_avg_error(function, factors, x, y):

    distances = []

    if len(factors) == 1:
        for i in range(0, len(x)):
            distances.append(abs((factors[0] * function(x[i])) - y[i]))

    else:
        for i in range(0, len(x)):
            distances.append(abs((factors[0] * function(x[i]) + factors[1]) - y[i]))
    return numpy.average(distances)


# Here starts our programm

logging.basicConfig(filename="logs.txt", level=logging.DEBUG, filemode='w')
logging.info("Start logging")

# Parser

parser = ArgumentParser()
parser.add_argument('class_module_name', help='Path to the class (something.something2.something3.className)'
                                              ' class must inherit from template class', type=str)
args = parser.parse_args()


try:
    my_class = my_import(args.class_module_name)
    my_object = my_class()

except ClassNotFoundException:
    print("Class not found")
    logging.info("Class not found")
    exit()


logging.debug("Created an object of my_class")

# function which counts time using timeit library - Timer function

for n in range(0, len(eny)):
    my_object.init(n)
    timer = timeit.Timer(my_object.function)
    t = timer.timeit(number=100)
    times.append(t)
    logging.debug("Time no. " + str(n) + " is " + str(t))

    if time.process_time() > 30.0:
        print("Limit time passed")
        eny = eny[:len(times)]
        break


coefficients.append(approximate(eny, times, 0))
logging.debug("Calculated linear approximation")
coefficients.append(approximate(eny, times, 1))
logging.debug("Calculated linear approximation")
coefficients.append(approximate(numpy.power(eny, 2), times, 1))
logging.debug("Calculated square approximation")
coefficients.append(approximate(numpy.power(eny, 3), times, 1))
logging.debug("Calculated cube approximation")
coefficients.append(approximate(numpy.log2(eny), times, 1))
logging.debug("Calculated logarithmic approximation")
coefficients.append(approximate(eny*numpy.log2(eny), times, 1))
logging.debug("Calculated n_logarithmic approximation")

errors.append(ultimate_avg_error(constant_function, coefficients[0], eny, times))
errors.append(ultimate_avg_error(linear_function, coefficients[1], eny, times))
errors.append(ultimate_avg_error(square_function, coefficients[2], eny, times))
errors.append(ultimate_avg_error(cube_function, coefficients[3], eny, times))
errors.append(ultimate_avg_error(log_function, coefficients[4], eny, times))
errors.append(ultimate_avg_error(nlogn_function, coefficients[5], eny, times))

logging.debug("Errors: " + str(errors))

index = errors.index(min(errors))
print("complexity_meter: " + complexity[index])
print("Function: " + functions[index])
print("Reverse function: " + rev_functions[index])
print("Coefficients: ")

if len(coefficients[index]) == 2:
    print("a: " + str(coefficients[index][0]))
    print("b: " + str(coefficients[index][1]))

else:
    print("a: " + str(coefficients[index][0]))

logging.debug("complexity_meter: " + complexity[index])
logging.debug("Function: " + functions[index])
logging.debug("Reverse function: " + rev_functions[index])

logging.debug("Finished")

# this was for testing approximated functions
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
