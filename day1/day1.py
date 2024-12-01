input_path = './input_day_1.txt'

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
            left_list.append(int(pair[0]))
            right_list.append(int(pair[1]))
        assert len(list_catalog[0]) == len(list_catalog[1]), 'Lists are of unequal length!'
    splitPairs(input_data)
    list_catalog[0].sort()
    list_catalog[1].sort()
    return list_catalog

def calculateDist(sorted_data = sortData(input_path)):
    '''Take sorted dataset and calculate difference between each element. Return integer of total difference across all pairs'''
    total_dist = 0
    for i in range(len(sorted_data[0])):
        total_dist += abs(sorted_data[0][i]-sorted_data[1][i])
    return total_dist

print(f'The summarized difference between all ID pairs are {calculateDist()}')

