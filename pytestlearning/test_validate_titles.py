import pytest

def test_validate_titles():

    expected_title = "Google.com"
    actual_title = "Google.com"
    test_title = "This is Gmsail Website"

    # if actual_title == expected_title:
    #     print("Test case Passed")
    # else:
    #     print("Test case failed")

    print("Begining")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmail" in test_title, "Gmail does not exists in title"
    assert False, "Forecefully failing the test"
    print("Ending")
