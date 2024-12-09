import re
input = './sample_data2.txt'


def readInput(path):
    '''read txt input and return string'''
    memory_string = open(path, 'r').read().rstrip()
    memory_string = 'do()' + memory_string  # ensure memory string starts with do()
    return memory_string


# def cleanMemory(memory_string):
#     '''iterate through string and remove slices between dont() and do() expressions. return new, clean string'''
#     do_pattern = r'do\(\)'
#     dont_pattern = r'don\'t\(\)'
#     do_indices = [match.start()
#                   for match in re.finditer(do_pattern, memory_string)]
#     dont_indices = [match.start()
#                     for match in re.finditer(dont_pattern, memory_string)]
#     index_pairs = []
#     for do_idx, dont_idx in zip(do_indices, dont_indices):
#         index_pairs.append((dont_idx, do_idx))
#     cleaned_memory = memory_string[:index_pairs[0]
#                                    [0]] + memory_string[index_pairs[-1][1]:]
#     for pair in index_pairs:
#         cleaned_memory += memory_string[pair[1]:pair[0]]
#         # cleaned_memory += memory_string[:pair[0]] + memory_string[pair[1]:]
#         # print(f'concatenated {memory_string[pair[0]:pair[1]]}')
#     return (cleaned_memory)


def findMul(memory_string):
    '''Iterate through string and return enabled muls'''
    pattern = r'mul\((\d+),(\d+)\)'
    muls_in_string = re.finditer(pattern, memory_string)
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    do_indices = [match.start()
                  for match in re.finditer(do_pattern, memory_string)]
    dont_indices = [match.start()
                    for match in re.finditer(dont_pattern, memory_string)]
    index_pairs = []
    for do_idx, dont_idx in zip(do_indices, dont_indices):
        index_pairs.append((dont_idx, do_idx))
    # print(index_pairs)
    for mul in muls_in_string:
        # if memory_string.rindex('do()', 0, memory_string[mul.span()[1]] > memory_string.rindex("don't()", 0, memory_string[mul.span()[1]])):
        #     print('det her if statement skal ikke være med mul.span. det skal evaluate på do og dont indices. Men jeg er for træt lige nu. Men det husker du lige, Henrik!')
        print(memory_string[mul.span()[1]])
    muls = ''
    return muls


def sumMuls(muls):
    sum_of_muls = sum(int(a) * int(b) for a, b in muls)
    return sum_of_muls


findMul(readInput(input))
# print(cleanMemory(readInput(input)))

# print(findMul(cleanMemory(readInput(input))))
