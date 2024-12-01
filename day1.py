

def readInput(path):
    '''Take path of txt file and return array of number pairs'''
    dist_array = []
    raw_input = open(path, 'r').readlines()
    for line in raw_input:
        dist_array.append(line.split())
    return dist_array



def sortData(raw_data):
    '''Take list of number pairs, and sort each element in ascending order, by first and second element respectively'''
    input_data = readInput(raw_data)
    left_list = []
    right_list = []
    list_catalog = [left_list, right_list]
    assert type(input_data) == list, 'Raw data should be a list!'
    def splitPairs(input_data):
        '''take list of number pairs and split them into two lists for easier sorting'''
        for pair in input_data:
            left_list.append(pair[0])
            right_list.append(pair[1])

sortData('./input_day_1.txt')
