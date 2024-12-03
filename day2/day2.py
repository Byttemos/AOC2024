input_path = './input_day2.txt'

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
    for digit in report:
        if digit in digit_cache:
            return True
            break
        else:
            digit_cache.append(digit)
    return False

def isMonotonic(report):
    '''takes a report and evaluates whether the sequence is monotonic. returns Boolean value'''
    subject = [i for i in report]
    asc = sorted(subject)
    desc = sorted(subject, reverse=True)
    if subject == asc or subject == desc:
        return True
    else:
        return False

def getSuccessiveDiff(report):
    '''evaluates the difference of successive elements in report, and returns the maximum difference'''
    report = [x for x in report]
    max_diff = 0
    for i in range(len(report)-1):
        current_diff = abs(report[i+1] - report[i])
        if current_diff > max_diff:
            max_diff = current_diff
    return max_diff

def removeNumsSafe(report):
    report = [int(x) for x in report]
    # for digit in report:
    #     temp_report = [x for x in report if x != digit]
    for i in range(len(report)):
        temp_report = [report[:i] + report[i+1:]]
        if getSuccessiveDiff(temp_report) < 4 and isMonotonic(temp_report) == True and hasDuplicates(temp_report) == False:
            return True

    return False


def getSafeReports(reports):
    safe_reports = 0
    for report in reports:
        if isMonotonic(report) == True and hasDuplicates(report) == False and getSuccessiveDiff(report) < 4: 
            safe_reports += 1
        elif removeNumsSafe(report) == True:
            safe_reports += 1
    return safe_reports

print(getSafeReports(readInput(input_path)))
