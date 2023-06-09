import check50
import statistics
import os
import re
import numpy as np



# Look up the values other than the mode in the student' answer and provide feedback. used in check50.Mismatch
def find_values(text,values):
    values=[str(i) for i in values]
    pattern = rf"{values[0]}|{values[1]}|{values[2]}|{values[3]}"

    matches = re.findall(pattern, text, re.IGNORECASE)
    found_values = set(matches)
    
    missing_values = set(values) - found_values
    if len(missing_values) == 0:
        help = "All statistics except the mode is correct. Check your find_mode() function."
        
    else:
        help = "Mismatch. Check both find_mode and stats(l) functions. The missing value(s) in addition to the mode:", ", ".join(missing_values)
    
    return(len(missing_values),help)

        
@check50.check()
def file_exists_check():
    """Check if the 'midterm1test.py' file exists"""
    if not os.path.isfile("midterm1test.py"):
        raise check50.Failure("The 'midterm1test.py' file does not exist")
 
@check50.check(file_exists_check)
def stats_check1():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '1.2, 2.0, 3.44, 4.1, 5.0'

    actual = check50.run("python3 midterm1test.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [1.2, 2.0, 3.44, 4.1, 5.0]
    ex_mean = statistics.mean(sample_list)
    ex_median = statistics.median(sample_list)
    ex_mode = float('nan')
    ex_stdv = statistics.stdev(sample_list)
    ex_range = max(sample_list) - min(sample_list)
    
    expected = f"Mean:\s*{ex_mean}\s*\nMedian:\s*{ex_median}\s*\nMode:\s*{ex_mode}\s*\nStandard deviation:\s*{ex_stdv}\s*\nRange:\s*{ex_range}"

    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
        help = ''
        missing_v, help1 = find_values(expected,[ex_mean, ex_median, ex_stdv, ex_range])
        if missing_v == 0:
            raise check50.Missing(ex_mode, actual, help=help1)
        else:
            raise check50.Mismatch(expected, actual, help=help1)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
        
@check50.check(file_exists_check)
def stats_check2():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '2.1, 2.1, 3.0, 4.0, 5.0, 5.0'

    actual = check50.run("python3 midterm1test.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [2.1, 2.1, 3.0, 4.0, 5.0, 5.0]
    ex_mean = statistics.mean(sample_list)
    ex_median = statistics.median(sample_list)
    ex_mode = 2.1
    ex_stdv = statistics.stdev(sample_list)
    ex_range = max(sample_list) - min(sample_list)
    
    expected = f"Mean:\s*{ex_mean}\s*\nMedian:\s*{ex_median}\s*\nMode:\s*{ex_mode}\s*\nStandard deviation:\s*{ex_stdv}\s*\nRange:\s*{ex_range}"    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
        help = ''
        missing_v, help1 = find_values(expected,[ex_mean, ex_median, ex_stdv, ex_range])
        if missing_v == 0:
            raise check50.Missing(ex_mode, actual, help=help1)
        else:
            raise check50.Mismatch(expected, actual, help=help1)
