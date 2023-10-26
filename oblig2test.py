import pytest
import oblig2main

def test_is_year_divided_with_4():
    assert oblig2main.is_Leap_year(2000) == True

def test_is_year_not_divided_with_100():
    assert oblig2main.is_Leap_year(2020) == True


def test_is_year_not_divided_with_4():
    assert oblig2main.is_Leap_year(1700) == False

def test_is_year_divided_with_100():
    assert oblig2main.is_Leap_year(1900) == False
