import numpy as np


def max_caloric(table):
    max_value = table[0]
    for row in table:
        if max_value[3] < row[3] or (max_value[3] == row[3] and str(max_value[1]) < str(row[1])):
            max_value = row

    return max_value[1]


def max_sugar(table):
    max_value = table[0]
    for row in table:
        if max_value[9] < row[9] or (max_value[3] == row[3] and str(max_value[1]) > str(row[1])):
            max_value = row

    return max_value[1]


def main():
    table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding='utf-8')

    max_caloric_name = max_caloric(table)
    max_sugar_name = max_sugar(table)
    print("1. Самый каллорийный продукт: " + max_caloric_name)
    print("2. Самый полезный по содержанию сахара: " + max_sugar_name)