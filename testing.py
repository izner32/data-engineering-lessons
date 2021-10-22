# LESSON 1-2 - UNIT TESTING AND INTEGRATION TESTING WITH PYTEST 

# LESSON 1.1 - WHAT IS UNIT TESTING 
"""
- software testing obviously catches bug 

levels of testing 
    unit testing 
        - testing at the function level 
        - unit test should be fast 
        - a test sohuld be written for each test case for a function 
    component testing 
        - testing is at the library and compiled binary level 
    system testing 
        - tests the external interfaces of a system which is a collection of sub-systems 
    performacne testings 
        - testing done at sub-system and system levels to verify timing and resource usages are acceptable 
"""
# example of unit testing 
import pytest 

# production code 
def str_len( theStr ):
    return len(theStr)

# unit test - setup -> action -> assert 
def test_string_length():
    testStr = "1" # setup 
    result = str_len(testStr) # action 
    assert result == 1 # assert or validate 

# LESSON 1.2 - WHAT IS TEST DRIVE DEVELOPMENT(TDD)
"""
- process where the devleoper takes personal responsibility for the quality of their code 
- unit tests are written before the production code 
- dont write all the test or production code at once 
- tests and production code are both written together in small bits of functionality 

tdd workflow 
red phase : write a failing unit test 
green phase: write just enough productino to make that test pass 
refactor phase: refactor the unit test and the production to make it clean 
repeat until the feature is complete 

3 laws of tdd 
- you may not write any production code until you have written a failing unit test 
- write just enough test to fail, failing to compile is failing
- write just enough code to pass 
"""

# example tdd: FizzBuzz Kata


# LESSON 3 - 