# Final Project: Factors Influencing Life Expectancy Rates.

# Proposal: 
* Using a dataset from Kaggle.com (Life Expectancy), our team will employ a variety of python techniques to identify various factors that influence the life expectancy rates in a given country (or countries).

## Technologies 
* This project will be developed using python 3 IDEs (such as VS Code, Jupyter Notebook, & PyCharm). 

## Setup 
* In order to run this file, please have the latest version of Python 3 downloaded.
* For the life_expectancy_cleaning.py file, please be sure to specify the filepath in where you would like to export the csv file after the dataframe changes.  
* To run the Final_Project_Life_Expectancy.py file, please open the python terminal and use the following: python Final_Project_Life_Expectancy.py NewLifeExpectancy.csv 

## File Purposes
* Life Expectancy.csv: Original Life Expectancy csv file without any changes made from Kaggle.com. 
* life_expectancy_cleaning.py: python file that includes code used to clean the original Life Expectancy csv file. 
* cleaned_life_expectancydf.csv: Life expectancy file after having bad/null data removed. This file and its' dataset will be used for the Final Project. 

## Annotated Bibliography (APA Format) 
* Rajarshi, K. (2018, February 10). Life Expectancy (WHO). Kaggle. https://www.kaggle.com/kumarajarshi/life-expectancy-who
   * CSV file that provides factors affecting life expectancy considering demographic variables, income composition, and mortality rate. Data from a period of 2000 to 2015 for        193 countries. The dataset will answer possible negative or positive correlation between life expectancy with year, polio, total expenditure, schooling, income composition      of resources, alcohol, diphtheria, adult Mortality, and population.

## Status Update (04/2/21)-Leek 
* Created the Project 4 ReadMe file.
* Added original Life Expectancy.csv file to team repository.
* Successfully cleaned the original life expectancy csv file, has been renamed into "cleaned_life_expectancydf.csv" and has been added to team repository.
* Created annotated bibliography on word document. Will complete once project has been finished.

## (4/4/21)-Leek
* Added Side effects to dropValues(): function in life_expectancy_cleaning.py. 

## (4/11/21)-Leek 
* Added Final_Project_Life_Expectancy.py file to team repository. 

## (4/14/21)-Joon 
* Added Annotated Bibliography for Life Expectancy.csv file 

## (4/14/21)-Josh
* Added method for our class and came up with the input idea for our dataframe.

## (4/14/21) Leek
* Added module docstring with succint description of what the project script does. 
* Added more details & arguments to calc_coefficient, population, adult_mortality, & diphtheria functions. 

## (4/16/21)-Leek
* Added details & returns to assigned functions docstrings.
* Addes side effects for all functions with a graphical output (or table).

## (4/16/21)- Owen
* Added details & returns to assigned functions docstrings.

## (4/16/21)- Josh
* Added details & returns to assigned functions docstrings.

## (4/16/21)- Joon
* Added details & returns to assigned functions docstrings.

## (4/23/21)- Josh
* Worked on the class and functions.
* Changed the check_input function into a method of the class.

## (4/28/21)- Owen
* Worked on making methods of functions
* Adjusted method docstrings

## (4/28/21) - Leek
* Added functiosn to class methods.

## (4/28/21) - Joon
* Added functions to class methods.
* Fixed annotated bibiography.

## (4/30/21) - Owen
* Added functions to my class methods
* Fixed line lengths on my sections
* Fixed some indentations on other sections (to meet 80 character limit)

## (4/30/21) - Joon
* Debugged method graphs not showing, added plt.show() to each factor method

## (4/30/21) - Leek
* Deleted cleaned_life_expectancy csv file, and created/added NewLifeExpectancy.csv file without null values. 

## (4/30/21) - Josh
* Worked more on the check_input method and got the name recognition of odd country names to pass
* Fixed other parts of the read_csv to make sure it can pass through all methods

## (5/4/21) - Josh
* Continue to work on the check_input method

## (5/4/21) - Owen
* Reformatted indentations for income_comp

## (5/5/21) - Josh
* Started working on the test scripts for our methods

## (5/5/21)- Leek
* Created & uploaded "Final Project Countries" word document (details what countries a user can input). 
* Created Final Project Presentation Power Point & uploaded to team repository. 

## (5/6/21) - Owen
* Attempted to fix pytest fixture
* Overall attempted to continue work on test scripting

## (5/7/21) - Josh
* Removed user_input where necessary, began pytest script. 

## (5/7/21) - Leek
* Created graph method, removed additional factors where necessary as well as function calls. 
* Created for loop for graph_list list (helps with graph method). 
