import Final_Project_Life_Expectancy as proj
import pytest
from unittest import mock
import builtins
import pandas as pd


class otherclass(proj.dframe):
    """ Testing validate_country, call separate from the init.
    """
    def __init__(self, filepath):
        """ Initializa otherclass object.

        Args:
            filepath (str): dataframe of the file 
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
    bosnia_and_herzegovina.check_input()
    assert bosnia_and_herzegovina.user_input == "Bosnia and Herzegovina"
    brazil.check_input()
    assert brazil.user_input == "Brazil"

def test_validate_country():
    with mock.patch("builtins.input", side_effect=["South Korea", "Brazil"]):
        instance = otherclass("NewLifeExpectancy.csv")
        instance.validate_country()
        assert instance.user_input == "Brazil"
    with mock.patch("builtins.input", side_effect=["Banana", "Bosnia and Herzegovina"]):
        instance2 = otherclass("NewLifeExpectancy.csv")
        instance2.validate_country()
        assert instance2.user_input == "Bosnia and Herzegovina"

class fakepair:
    """Testing graph method. 
    
    Attributes:
            args(list): position argument, checks if the position of the parameter is in the correct position. 
            kwargs(dict): Keyword argument, checks to see if the instance of the keyword arguments is in the correct place. 
    """
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
    