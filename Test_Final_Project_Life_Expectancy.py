import Final_Project_Life_Expectancy as proj
import pytest
from unittest import mock
import builtins

#Create the class
class test_dframe:
    
    def test___init__():
        with mock.patch("builtins.input", side_effect=["Algeria"]):
            assert proj.__init__() == ("Algeria")
    
    def test_read_dframe():
    
    
    def test_check_input():

        
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

#@pytest.fixture
#def afghan_test():
    #return dframe.year("Afghanistan")
    #call in file handle?