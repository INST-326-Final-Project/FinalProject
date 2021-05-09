import Final_Project_Life_Expectancy as proj
import pytest
from unittest import mock
import builtins
import pandas as pd


class otherclass(proj.dframe):
    """ Testing validate_country, call separate from the init
    """
    def __init__(self, filepath):
        """ User inputs the country name. Will include each row with the country
        name and for each year it shows up for.

        Args:
            filepath (str): dataframe of the file
            
        Returns:
            user_input(str): name of the country
        """
        self.df = pd.read_csv(filepath)


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
    # bosnia_and_herzegovina.check_input()
    # assert bosnia_and_herzegovina.check_input == "Bosnia and Herzegovina" #Prof said to fix this Josh
    brazil.check_input()
    assert brazil.check_input == "Brazil"

def test_validate_country():
    with mock.patch("builtins.input", side_effect=["South Korea", "Brazil"]):
        instance = otherclass("NewLifeExpectancy.csv")
        instance.validate_country()
        assert instance.user_input == "Brazil"

class fakepair:
    def __init__(self):
        self.args = []
        self.kwargs = { }
    
    def pairpair(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
def donothing():
    pass

def test_graph(brazil, monkeypatch):
    monkeypatch.setattr(proj.plt,"show", donothing) #replace attribute show with donothing

    f = fakepair()
    monkeypatch.setattr(proj.sns, "pairplot", f.pairpair)  
    brazil.graph("Polio")
    assert isinstance(f.args[0], pd.DataFrame)
    assert isinstance(f.kwargs["x_vars"], list) #checking the kwargs this time. 

def test_parse_args():
    with pytest.raises(SystemExit):
        proj.parse_args(["a", "b"])
    with pytest.raises(SystemExit):
        proj.parse_args([])
    var = proj.parse_args(["a"])
    assert var.filepath == "a"
    