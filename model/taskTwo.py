import numpy as np


def check():
    pass


def generation_line(line):
    line = np.insert(np.append(line, np.array([0, 0])), 0, np.array([0, 0]))
    res = np.array([], int)
    for i in range(1, len(line)-1):
        if line[i-1] == 1 and line[i] == 1 and line[i+1] == 1:
            res = np.append(res, 0)
        elif line[i-1] == 1 and line[i] == 1 and line[i+1] == 0:
            res = np.append(res, 0)
        elif line[i-1] == 1 and line[i] == 0 and line[i+1] == 1:
            res = np.append(res, 0)
        elif line[i-1] == 1 and line[i] == 0 and line[i+1] == 0:
            res = np.append(res, 1)
        elif line[i-1] == 0 and line[i] == 1 and line[i+1] == 1:
            res = np.append(res, 1)
        elif line[i-1] == 0 and line[i] == 1 and line[i+1] == 0:
            res = np.append(res, 1)
        elif line[i-1] == 0 and line[i] == 0 and line[i+1] == 1:
            res = np.append(res, 1)
        elif line[i-1] == 0 and line[i] == 0 and line[i+1] == 0:
            res = np.append(res, 0)

    return res


def main():
    print("Работаем!")
    life = np.array([int(i) for i in input().split()])
    for i in range(10):
        life = generation_line(life)
        print(life)