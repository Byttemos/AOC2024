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
    def findM(i, j):
        '''take matrix indexed position of X and look for remaining letters in all directions'''
        def checkDirection(dir):
            print(dir)

        if data_array[i-1][j] == 'M':
            print('M found due N')
        if data_array[i][j-1] == 'M':
            print('M found due W')
        if data_array[i-1][j-1] == 'M':
            print('M found NW')
        if data_array[i+1][j] == 'M':
            print('M found due S')
        if data_array[i][j+1] == 'M':
            print('M found due E')
        if data_array[i+1][j+1] == 'M':
            print('M found SE')
        if data_array[i+1][j-1] == 'M':
            print('M found SW')
        if data_array[i-1][j+1] == 'M':
            print('M found NE')

    for i in range(data_array.shape[0]):
        for j in range(data_array.shape[1]):
            if data_array[i][j] == 'X':
                findM(i, j)


findX(readInput(sample_path))
