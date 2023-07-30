

import pytest

@pytest.mark.integration
def test_create_booking_tc1():
    assert True == True

@pytest.mark.integration
def test_create_booking_tc2():
    assert True == False

@pytest.mark.integration
def test_create_booking_tc3():
    assert True == True


#pytest Ttest_scripts/* -s -v --alluredir=./reports --html=report.html
