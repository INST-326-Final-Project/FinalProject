#Import necessary modules. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as st

#Create the class
class dframe:
    """Instantiate events happening from their years, months, days, & descriptions.  
    
    Attributes:
        user_input(str): user inputs the country name. Value
        will be passed into the check_input function. 
    """
    
    def __init__(self, user_input):
        """ User inputs the country name. 

            Args:
                user_input(str): country name the user inputs. 
        """
    
def check_input():
    """Check the users input and capitalize the country names. Uses the user 
    input to see what specific country/row it is working with.

        Args:
            user_input(str): The users' input. 
        
        Returns:
            print(str): Return the users input if the country name is incorrectly spelled, or doesn't
            exist within the dataset. 
        
        Side effects:
            prints to stdout.   
    """

def year():
    """Display a graph of a country's year factor influencing life expectancy.  
    
    """

def polio():
    """Display a graph of a country's polio factor influencing life expectancy.  
    
    """

def total_exp():
    """Display a graph of a country's total expenditure factor influencing life expectancy.
    
    """

def schooling():
    """Display a graph of a country's schooling factor influencing life expectancy.
    
    """

def income_comp():
    """Display a graph of a country's Income composition of resources factor influencing life expectancy.
    
    """

def alcohol():
    """Display a graph of a country's alcohol consumption factor influencing life expectancy.
    
    """ 

def diphtheria():
    """Display a graph of a country's diphtheria factor influencing life expectancy.
    
    """ 

def adulty_mortality():
    """Display a graph of a country's adult mortality factor influencing life expectancy.
    
    """ 

def population():
    """Display a graph of a country's population factor influencing life expectancy.
    
    """

def calc_coefficient():
    """Calculate the coefficient (linear regression) for the specified country. 
    
    """
