import pytest
import os
from algorithms import insertion_sort

# Create fixture to load test data only once for module
@pytest.fixture(scope="module")
def get_testdata():
    lists = []
    try:
        with open(os.path.join("tests", "algorithm_test_data.txt"), "r") as data:
            line_num = 1
            for line in data.readlines():
                line = line.strip()
                if line == "":
                    continue

                try:
                    lists.append([int(val.strip()) for val in line.split(",")])
                
                except ValueError:
                    print(f"Error in algorithm_test_data.txt line {line_num}, not a number.")
                    raise

                line_num += 1
                
    
    except FileNotFoundError:
        print("Fatal error: no test data file!")
        raise
    
    return lists
    

def test_insertion_sort(get_testdata):
    for case in get_testdata:
        assert insertion_sort.sort(case) == sorted(case)