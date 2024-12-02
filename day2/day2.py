input_path = './sample_input_day2.txt'

def readInput(path):
    raw_input = open(path, 'r').readlines()
    report_array = []
    for line in raw_input:
        report_array.append(line.split())
        for char in line:
            char = int(char)

    return report_array
readInput(input_path)
