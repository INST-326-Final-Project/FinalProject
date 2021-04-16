"""
Script takes the users input and outputs information & data on a country. 
"""
#Import necessary modules.
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as st

#Create the class
class dframe:
   """Instantiate events happening from their years, months, days, & 
    descriptions. 
    
    Attributes:
        user_input(str): user inputs the country name. Value
            will be passed into the check_input function.
    """
    
    def __init__(self, user_input):
        """ User inputs the country name. Will include each row with the country
        name and for each year it shows up for.

            Args:
                user_input(str): country name the user inputs.
                
            Returns:
                user_input(str): name of the country
        """
    
    def read_dframe(self, filepath):
        """Method that reads in the "cleaned_life_expectancydf.csv" file and 
        creates a dataframe with pandas based on the dataset.
        
            Args:
                filepath (str): the "cleaned_life_expectancydf.csv" file
                
            Returns:
                  dataframe: dataframe of the csv file. This dataframe contains 
                193 country names, alongside their associated factors. This is 
                a requirement to run the file. 
        """
    
def check_input(user_input):
    """Check the users input and capitalize the country names. Uses the user 
    input to see what specific country/row it is working with. Will have 
    possible user input names for countries and will correct them if the 
    capitalization is wrong.

        Args:
            user_input(str): country name the user inputs. 
        
        Returns:
            print(str): Return the users input if the country name is 
            incorrectly spelled, or doesn't exist within the dataset.  
        
        Side effects:
            prints to stdout.   
    """

def year():
    """Display a graph of a country's year factor influencing life expectancy. 
    Years range from 2000 to 2015 for each country.  
    
        Args:
            user_input(str): country name the user inputs.
    """

def polio():
    """Display a graph of a country's polio factor influencing life expectancy.
    Polio (Pol3) immunization coverage among 1-year-old infants.
    
        Args:
            user_input(str): country name the user inputs.
    """

def total_exp():
    """Display a graph of a country's total expenditure factor influencing life 
    expectancy.
    General government expenditure on health as a percentage of total government 
    expenditure. 
    
        Args:
            user_input(str): country name the user inputs.
    """

def schooling():
    """Display a graph of a country's schooling factor influencing life 
        expectancy.
        
    Args:
        user_input(string): The country that schooling will be analyzed and 
            derived from
    
    Returns:
        A graph of the regression betweeen schooling and life expectency
    """

def income_comp():
    """Display a graph of a country's Income composition of resources factor 
        influencing life expectancy.

    Args:
        user_input(string): The country that the income_comp will be derived 
            from
    
    Returns:
        A graph of the regression between income_comp and life expectency
    """

def alcohol():
    """Display a graph of a country's alcohol consumption factor influencing 
    life expectancy. Will analyze the affect of this factor on the independent 
    variable
    
    Args:
        user_input(str): The name of the country that this is being analyzed on
    
    Returns:
        A graph of the regression between alcohol and life expectency
    """ 

def diphtheria():
    """Display a graph of a country's diphtheria factor influencing life expectancy.
    shows the factor of Diptheria tatnus toxoid & pertussis (DTP3) immunization 
    amongst young children (1-year olds).
        
        Args:
            user_input(str): country name the user inputs.
    """ 

def adulty_mortality():
    """Display a graph of a country's adult mortality factor influencing life expectancy.
    Adult mortality rates are presented as the probablility of dying between the 
    ages of 15 to 60 per 1000 population. 
    
        Args:
            user_input(str): country name the user inputs.
    """ 

def population():
    """Display a graph of a country's population factor influencing life expectancy. 
    Populations range within the million to tens of millions. 
    
        Args:
            user_input(str): country name the user inputs.
    """

def calc_coefficient():
    """Calculate the coefficient (linear regression) for the specified country. 
    This will use the statsmodels.api module to show linear regression model
    for each factor in the csv file. Results will include respective p-values 
    (values thata re less than 0.05 are considered statistically significant).
    
        Args:
            user_input(str): country name the user inputs.
    """

 
def main():
    """Main function
    
    """
    
    
if __name__ == "__main__":
    main(sys.argv[1])
