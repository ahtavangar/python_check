import check50
import statistics
import os
import re
import numpy as np
'''
def find_mode(data):
    myList = [float(i) for i in data.split(",")]
    mode = statistics.mode(myList)

    # Check if there is a unique mode
    if np.unique(myList, return_counts=True)[1].max() == 1:
        return float("nan")
    return mode
'''
@check50.check()
def file_exists_check():
    """Check if the 'midterm1test.py' file exists"""
    if not os.path.isfile("midterm1test.py"):
        raise check50.Failure("The 'midterm1test.py' file does not exist")
'''
@check50.check(file_exists_check)
def mode_check():
    """Check the output of the find_mode(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list0 = '2, 2, 3, 4, 5'

   
    actual = check50.run("python3 midterm1test.py").stdin(sample_list0).stdout().exit(0)
    # Retrieve the expected values using the statistics module
    sample_list0 = [2.0,2.0,3.0,4.0,5.0]
        
    expected = f"Mode: {find_mode(sample_list0)}"
    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual):
        help = "The find_mode(l) function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
'''        
@check50.check(file_exists_check)
def stats_check1():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '1, 2, 3, 4, 5'

    actual = check50.run("python3 midterm1test.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [1.0,2.0,3.0,4.0,5.0]
    expected_mean = statistics.mean(sample_list)
    expected_median = statistics.median(sample_list)
    expected_mode = float('nan')
    expected_stdv = statistics.stdev(sample_list)
    expected_range = max(sample_list) - min(sample_list)
    
    expected = f"Mean:\s*{expected_mean}\s*\nMedian:\s*{expected_median}\s*\nMode:\s*{expected_mode}\s*\nStandard deviation:\s*{expected_stdv}\s*\nRange:\s*{expected_range}"

    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
        help = "The stats(l) function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
        
@check50.check(file_exists_check)
def stats_check2():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '2, 2, 3, 4, 5, 5, 5'

    actual = check50.run("python3 midterm1test.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [2.0,2.0,3.0,4.0,5.0,5.0,5.0]
    expected_mean = statistics.mean(sample_list)
    expected_median = statistics.median(sample_list)
    expected_mode = 5.0
    expected_stdv = statistics.stdev(sample_list)
    expected_range = max(sample_list) - min(sample_list)
    
    expected = f"Mean:\s* {expected_mean}\s* \nMedian:\s* {expected_median}\s* \nMode:\s* {expected_mode}\s* \nStandard deviation:\s* {expected_stdv}\s* \nRange:\s* {expected_range}"
    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
        help = "The stats(l) function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
