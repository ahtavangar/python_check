import check50
import os
import re

# this function checks if all values in a dictionary output are present in the student's output
def findAllValues(number_list, actual):
    found = all(number in actual for number in number_list)
    if found:
        help = 'all statistics values are correct but the output does not have a correct format.'
    else:
        help = ''
    return (found, help)

@check50.check()
def file_exists_check():
    """Check if the 'Assignment_3.py' file exists"""
    if not os.path.isfile("Assignment_3.py"):
        raise check50.Failure("The 'Assignment_3.py' file does not exist")
 
@check50.check(file_exists_check)
def calculate_statistics_check1():
    """Check the output of the calculate_statistics function from extract_financials() for MidtermFinancialReport.txt""" # file provided to students
    
    check50.include("MidtermFinancialReport.txt")
    assert os.path.exists("MidtermFinancialReport.txt")

    actual = check50.run("python3 Assignment_3.py").stdin('MidtermFinancialReport.txt').stdout()
    expected = "1234567.0" # "The minimum reveue across all locations is 1234567.0."
        
    if not re.search(expected, actual):
        help = "check calculate_statistics() function"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("Your answer does not include the correct output for the minimum reveue across all locations.")

@check50.check(file_exists_check)
def calculate_statistics_check2():
    """Check the output of the calculate_statistics function from extract_financials() for MidtermFinancialReport.txt""" # file provided to students
    
    check50.include("MidtermFinancialReport.txt")
    assert os.path.exists("MidtermFinancialReport.txt")

    actual = check50.run("python3 Assignment_3.py").stdin('MidtermFinancialReport.txt').stdout()
    expected = "20543148.0" # "The mean expenses across all locations is 20543148.0."
        
    if not re.search(expected, actual):
        help = "check calculate_statistics() function"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("Your answer does not include the correct output for mean expenses across all locations.", help = help)    
        
@check50.check(file_exists_check)
def extract_financials_check1():
    """Check the output of the extract_financials() and calculate_statistics() functions for the net profit statistics across all locations for MidtermFinancialReport.txt""" # file provided to students
    
    check50.include("MidtermFinancialReport.txt")
    assert os.path.exists("MidtermFinancialReport.txt")

    actual = check50.run("python3 Assignment_3.py").stdin("MidtermFinancialReport.txt").stdout()
    expected = "{'Mean': 3950746.35, 'Median': 3105000.5, 'Mode': 1666667.0, 'Standard Deviation': 3128996.141825821, 'Minimum': 246913.0, 'Maximum': 10433333.0, 'Range': 10186420.0}"
        
    if not re.search(expected, actual):
        expected_values = ['3950746.35', '3105000.5', '1666667.0', '3128996.141825821', '246913.0', '10433333.0', '10186420.0']
        found, help = findAllValues(expected_values, actual)
        if found == True:
            raise check50.Mismatch(expected, actual, help=help)
        raise check50.Failure("extract_financials() function does not produce the correct output.")
        
        
@check50.check(file_exists_check)
def extract_values_check2():
    """Check the output of the extract_financials() function for the last three dictionary keys for MidtermFinancialReport.txt""" # file provided to students
    
    check50.include("MidtermFinancialReport.txt")
    assert os.path.exists("MidtermFinancialReport.txt")

    actual = check50.run("python3 Assignment_3.py").stdin("MidtermFinancialReport.txt").stdout()
    expected = "['Location19', 'Location20', 'Statistics']"
        
    if not re.search(expected, actual):
        help = "Make sure the keys are returned in a list."
        raise check50.Mismatch(expected, actual, help=help)
        
        #raise check50.Failure("Your answer does not include the correct output for the last three keys in the financials dictionary.", help = help)
        
