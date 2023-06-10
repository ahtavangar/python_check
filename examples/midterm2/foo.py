import check50
import os
import re




@check50.check()
def file_exists_check():
    """Check if the 'Assignment_2.py' file exists"""
    if not os.path.isfile("Assignment_2.py"):
        raise check50.Failure("The 'Assignment_2.py' file does not exist")
 
@check50.check(file_exists_check)
def read_text_check1():
    """Check the output of the read_text() function"""
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_2.py").stdin('sample.txt').stdout()
      
    expected = r"\s*- Revenue: $1,234,567"
    #display version of expected to show when error raised
    #expected_dis = f"Mean: {ex_mean}\nMedian: {ex_median}\nMode: {ex_mode}\nStandard deviation: {ex_stdv}\nRange: {ex_range}"
    
    if not re.search(expected, actual):
        help = "read_text() function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("read_text() function does not produce the correct output")

@check50.check(file_exists_check)
def extract_values_check1():
    """Check the output of the extract_values() function"""
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_2.py").stdin('sample.txt').stdout()
      
    expected = "1234567.0"
    #display version of expected to show when error raised
    #expected_dis = f"Mean: {ex_mean}\nMedian: {ex_median}\nMode: {ex_mode}\nStandard deviation: {ex_stdv}\nRange: {ex_range}"
    
    if not re.search(expected, actual):
        help = "extract_values() function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
        
        
@check50.check(file_exists_check)
def extract_values_check2():
    """Check the output of the extract_values() function"""
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_2.py").stdin('sample.txt').stdout()
      
    expected = "{'Revenue': 2345678.0, 'Expenses': 1876543.0, 'Net Profit': 469135.0, 'Units Sold': 15000.0, 'Average Unit Price': 156.42}"
    #display version of expected to show when error raised
    #expected_dis = f"Mean: {ex_mean}\nMedian: {ex_median}\nMode: {ex_mode}\nStandard deviation: {ex_stdv}\nRange: {ex_range}"
    
    if not re.search(expected, actual):
        help = "extract_values() function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
        
