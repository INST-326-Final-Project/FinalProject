import Final_Project_Life_Expectancy as proj
import pytest
from unittest import mock
import builtins


@pytest.fixture
def algeria():
    with mock.patch("builtins.input", side_effect=["Algeria"]):
        instance1 = proj.dframe("NewLifeExpectancy.csv")
    return instance1

@pytest.fixture
def bosnia_and_herzegovina():
    with mock.patch("builtins.input", side_effect=["bosnia and herzegovina"]):
        instance1 = proj.dframe("NewLifeExpectancy.csv")
    return instance1

@pytest.fixture
def brazil():
    with mock.patch("builtins.input", side_effect=["BRAZIL"]):
        instance1 = proj.dframe("NewLifeExpectancy.csv")
    return instance1

def test_check_input(algeria, bosnia_and_herzegovina, brazil):
    algeria.check_input()
    assert algeria.user_input == "Algeria"
    bosnia_and_herzegovina.check_input()
    assert bosnia_and_herzegovina.check_input == "Bosnia and Herzegovina"
    brazil.check_input()
    assert brazil.check_input == "Brazil"
        
def test_year():
        

def test_polio():
    

def test_total_exp():


def test_schooling():


def test_income_comp():


def test_alcohol():

    
def test_diphtheria():


def test_adult_mortality():


def test_population():


def test_calc_coefficient():

