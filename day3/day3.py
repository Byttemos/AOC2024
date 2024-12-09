import re
input = './data.txt'


def readInput(path):
    '''read txt input and return string'''
    memory_string = open(path, 'r').read().rstrip()
    memory_string = 'do()' + memory_string  # ensure memory string starts with do()
    return memory_string


def findMul(memory_string):
    '''Iterate through string and return accumulated multiplication of enabled muls'''
    pattern = r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))'
    muls_in_string = re.findall(pattern, memory_string)
    activated = True
    sum_of_muls = 0
    for p in muls_in_string:
        if p[2] == 'do()':
            activated = True
            continue
        if p[3] == "don't()":
            activated = False
            continue
        if activated == True:
            sum_of_muls += int(p[0]) * int(p[1])
    return sum_of_muls


findMul(readInput(input))
