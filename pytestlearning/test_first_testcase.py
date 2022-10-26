import pytest

def setup_module(module):
    print("Creating DB Connection")

def teardown_module(module):
    print("Closing DB Connection")

def setup_function(function):
    print("Launching browser")
def test_doLogin():
    print("Executing Login Test case")
    print("Completed Login Test case")

def test_doRegister():
    print("Executing Register Test case")

#Test Case

def teardown_function(function):
    print("Closing browser")