input_path = './sample_input_day2.txt'

def readInput(path):
    '''read input from txt file and return 2d array of reports'''
    raw_input = open(path, 'r').readlines()
    report_array = []
    for line in raw_input:
        int_chars = line.split()
        numbers = []
        for int_char in int_chars:
            number = int(int_char)
            numbers.append(number)
        report_array.append(numbers)
    return report_array

def hasDuplicates(report):
    '''Takes single report and returns True if it contains duplicates, False if it doesnt'''
    digit_cache = []
    for digit in str(report):
        if digit in digit_cache:
            return True
            break
        else:
            digit_cache.append(digit)
    return False

def isMonotonic(report):
    '''takes a report and evaluates whether the sequence is monotonic. returns Boolean value'''
    subject = [int(i) for i in str(report)]
    asc = sorted(subject)
    desc = sorted(subject, reverse=True)
    if subject == asc or subject == desc:
        return True
    else:
        return False

def getSuccessiveDiff(report):
    '''evaluates the difference of successive elements in report, and returns the maximum difference'''
    max_diff = 0
    for i in range(len(report)-1):
        current_diff = abs(report[i+1] - report[i])
        if current_diff > max_diff:
            max_diff = current_diff
    return max_diff
        


def getReportSafety(reports):
    '''Take list of reports and return a safety score of how many reports are considered safe'''
    safety_score = 0
    for report in reports:
        for digit in report:
            if digit == report[digit+1]: #if next element is same
                break #not safe
            elif digit < report[digit+1]: #if next element is larger
                if digit < report[digit-1]: #THEN if previous element is also larger
                    break #not safe
            elif digit > report[digit+1]: #if next element is smaller
                if digit > report[digit-1]: #THEN if previous element is also smaller
                    break #not safe
            else:
                safety_score += 1
    return safety_score





# print(getReportSafety(readInput(input_path)))
for report in readInput(input_path):
    hasDuplicates(report)
