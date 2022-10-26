import pytest


def get_data():

    return [
        ("trainer@test.com","sdfffsf"),
        ("helper@test.com", "sdxvvfffsf"),
        ("user@test.com", "gdgdfgsf")
    ]



@pytest.mark.parametrize("username,password", get_data())
def test_doLogin(username, password):
    print(username,"---",password)