import re
input = './sample_data2.txt'

def readInput(path):
    '''read txt input and return string'''
    memory_string = open(path, 'r').read().rstrip()
    return memory_string

def cleanMemory(memory_string):
    '''iterate through string and remove slices between dont() and do() expressions. return new, clean string'''
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'n\(\)'
    do_indices = [match.start() for match in re.finditer(do_pattern, memory_string)]
    dont_indices = [match.start() for match in re.finditer(dont_pattern, memory_string)]
    index_pairs = []
    for do_idx, dont_idx in zip(do_indices, dont_indices):
        index_pairs.append((dont_idx, do_idx))
    return(index_pairs)

def findMul(memory_string):
    '''Iterate through string and return the sum of all multiplications found'''
    pattern = r'mul\((\d+),(\d+)\)'
    matches_in_string = re.findall(pattern, memory_string)
    sum_of_muls = sum(int(a) * int(b) for a, b in matches_in_string)
    return sum_of_muls
 

print(findMul(readInput(input)))
