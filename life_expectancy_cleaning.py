#This program will clean out the bad data in the life expectancy csv file.
#Import pandas module.
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def dropValues():
    """Read and drop any missing/null values from the dataset."""
    clean_dataset = pd.read_csv("Life Expectancy.csv", sep=",")
    #Drop null values using the dropna() method.
    clean_dataset.dropna()
    #Drop all columns with incorrect/bad data.
    clean_dataset.drop(['Status','infant deaths', 'percentage expenditure', 'Hepatitis B', 'Measles ',
                                 'under-five deaths ', ' HIV/AIDS', 'GDP', ' thinness  1-19 years', ' thinness 5-9 years',' BMI '], axis=1, inplace = True)
    #Export the cleaned dataset. User must specify their file path in order to export the new dataframe.
    clean_dataset.to_csv(r'C:\Users\virtu\PycharmProjects\INST326\cleaned_life_expectancydf.csv', index = False, header=True)
    print(clean_dataset)
#Call the function
dropValues()
