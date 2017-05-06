from math import log, sqrt
import time
import numpy
import timeit
import matplotlib.pyplot as plt
from random import randint
import tkinter
import math
import logging


eny = [25, 50, 75, 100, 125, 150, 175, 200, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]
times = []
array = []


# sums = []

# x = numpy.array([1, 7, 20, 50, 79])
# y = numpy.array([10, 19, 30, 35, 51])
# print(numpy.polyfit(x*numpy.log2(x), y, 1))



def function(n):
    list = range(0, n)
    bubbleSort(list)




def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp



# TO DO tutaj bedzie mierzenie czasów


# TO DO tutaj bedzie obliczanie wspolczynnikow

def approximate(a, b, n):
    return numpy.polyfit(a, b, n)

# funkcje liczace srednie kwadratowe


def square_root_avg_error(factor, x, y):
    distances = []
    for i in range(0, len(x)):
        distances.append(abs((factor[0]*sqrt(x[i]) + factor[1]) - y[i]))
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


def perform():

    for i in range(0, len(eny)):
        print(eny[i])
        t = timeit.timeit(stmt="function(" + str(eny[i]) + ")", setup="from __main__ import function", number=1)
        times.append(t)
        logging.debug("Time no. " + str(i) + " is " + str(t))

# Tutej niech sie zaczyna main tak jakby


logging.basicConfig(filename="logs.txt", level=logging.DEBUG)
logging.info("Start logging")

# liczenie wsplczynikow funkcji
perform()

square_root = approximate(numpy.sqrt(eny), times, 1)
logging.debug("Calculated square_roo approximation")
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

print(square_root)
print(constant)
print(linear)
print(square)
print(cube)
print(logarithmic)
print(n_logarithmic)

plt.plot(eny, times)
plt.show()


square_root_avg = square_root_avg_error(square_root, eny, times)
constant_avg = constant_avg_error(constant, eny, times)
linear_avg = linear_avg_error(linear, eny, times)
square_avg = square_avg_error(square, eny, times)
cube_avg = cube_avg_error(cube, eny, times)
logarithmic_avg = logarithm_avg_error(logarithmic, eny, times)
n_logarithmic_avg = n_logarithm_avg_error(n_logarithmic, eny, times)

print(square_root_avg, constant_avg, linear_avg, square_avg, cube_avg, logarithmic_avg, n_logarithmic_avg)
print(min(square_root_avg, constant_avg, linear_avg, square_avg, cube_avg, logarithmic_avg, n_logarithmic_avg))

print(square_root_avg, constant_avg, linear_avg, logarithmic_avg, n_logarithmic_avg)
print(min(square_root_avg, constant_avg, linear_avg, logarithmic_avg, n_logarithmic_avg))

logging.debug("Finished")
