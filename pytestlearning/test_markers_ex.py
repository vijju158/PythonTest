import pytest

@pytest.mark.functional
def test_Login():
    print("Executing Login Test case")

@pytest.mark.regression
def test_Register():
    print("Executing Register Test case")


@pytest.mark.smoke
def test_email():
    print("Executing Email Test case")

@pytest.mark.skip
def test_skip():
    print("Executing Skip Test case")