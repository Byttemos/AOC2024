#!/usr/bin/env python3
import numpy as np

sample_path = './sample_data.txt'
path = './data.txt'


def readInput(data_path):
    '''Take text input and return 2d np array of the puzzle characters'''
    with open(data_path, 'r') as file:
        data = [line.strip() for line in file]
    data_array = np.array([list(line) for line in data])
    return data_array

def findX(data_array):
    '''Take data array and return and call findMAS on all positions of X'''
    # print(f'received input: {data_array}')
    def findMAS(i, j):
        '''take matrix indexed position of X and look for remaining letters in all directions'''
        print(data_array[i][j])
    for i in range(data_array.shape[0]):
        # print(f'Checking row: {i}')
        for j in range(data_array.shape[1]):
            # print(f'Checking column: {j}')
            if data_array[i][j] == 'X':
                findMAS(i, j)


findX(readInput(sample_path))
