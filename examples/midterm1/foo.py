from check50 import *
import statistics
import os

@check
def file_exists_check():
    """Check if the 'midterm1.py' file exists"""
    if not os.path.isfile("midterm1.py"):
        raise Failure("The 'midterm1.py' file does not exist")

@check
def stats_check():
    """Check the output of the stats(l) function"""
    # Define a sample list to test the stats(l) function
    sample_list = [1, 2, 3, 4, 5]

    # Call the stats(l) function from the "midterm1.py" file
    try:
        import midterm1
        stats_output = midterm1.stats(sample_list)
    except Exception as e:
        raise Failure(f"Error while calling stats(l) function: {e}")

    # Retrieve the expected values using the statistics module
    expected_mean = statistics.mean(sample_list)
    expected_median = statistics.median(sample_list)
    expected_stdv = statistics.stdev(sample_list)
    expected_range = max(sample_list) - min(sample_list)

    # Compare the expected values with the stats(l) output
    if stats_output != f"Mean: {expected_mean} \nMedian: {expected_median}\nStandard deviation: {expected_stdv} \nRange: {expected_range}":
        raise Failure("The stats(l) function does not produce the correct output")
    print("Your code passed the stats_check!")

