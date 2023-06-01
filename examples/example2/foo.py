import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_1.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    actual = check50.run("python3 Assignment_1.py").stdout()
    expected = "female    6\nmale      4"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for first value_counts() print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    actual = check50.run("python3 Assignment_1.py").stdout()
    expected = "female    9\nmale      3"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for second value_counts() print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    actual = check50.run("python3 Assignment_1.py").stdout()
    expected = "The group of students with the highest mean scores in math, writing, and reading had a majority of female students."
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for final conclusion sentence."
        raise check50.Missing("Correct results",'your output',help=help)

    
