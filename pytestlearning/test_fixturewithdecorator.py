import pytest


@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")

@pytest.fixture(scope='function')
def before():
    print("Launching browser")

    yield
    print("Closing browser")


# def test_doLogin(setup,before):
#     print("Executing Login Test case")
#     print("Completed Login Test case")
#
# def test_doRegister(setup,before):
#     print("Executing Register Test case")


@pytest.mark.usefixtures("setup","before")
def test_doLogin():
    print("Executing Login Test case")
    print("Completed Login Test case")

@pytest.mark.usefixtures("setup","before")
def test_doRegister(setup,before):
    print("Executing Register Test case")
