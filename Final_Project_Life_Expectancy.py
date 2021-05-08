"""
Script takes the users input and outputs information & data on a country. 
"""
#Import necessary modules.
from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as st
import sys
import seaborn as sns



#Create the class
class dframe:
    """Instantiate events happening from their years, months, days, & 
    descriptions. 
    
    Attributes:
        user_input(str): user inputs the country name. Value
            will be passed into the check_input function.
    """
    
    def __init__(self, filepath):
        """ User inputs the country name. Will include each row with the country
        name and for each year it shows up for. Initialize dframe object.
            
            Args:
                filepath (str): dataframe of the file
        """
        self.df = pd.read_csv(filepath)
        self.validate_country()
        
    
    def read_dframe(self):
        """Method that reads in the "cleaned_life_expectancydf.csv" file and 
        creates a dataframe with pandas based on the dataset.
                
            Returns:
                  dataframe: dataframe of the csv file. This dataframe contains 
                193 country names, alongside their associated factors. This is 
                a requirement to run the file. 
            
            Side effects:
        """
        
        # prints the 15 rows from the dataframe for that country
        output = print(self.df[self.df["Country"] == self.user_input])
        
        return output

    def check_input(self):
        """Check the users input and capitalize the country names. Uses the user 
        input to see what specific country/row it is working with. Will have 
        possible user input names for countries and will correct them if the 
        capitalization is wrong. Fixes upper/lowercase syntax and for unique 
        words.

            Args:
                user_input(str): country name the user inputs. 
        
            Returns:
                print(str): Return the users input if the country name is 
                incorrectly spelled, or doesn't exist within the dataset.  
        
            Side effects:
                prints to stdout.   
        """
        
        final_title = []
        always_lower = ["in", "and", "of", "former", "the"]
        
        # if the input is not in the country column
        if (self.user_input not in self.df["Country"].values):
            lower = self.user_input.lower()
            templist = lower.split(" ")
            
            # account for special words that are lowercase
            for i in templist:
                if i not in always_lower:
                    i = i.title()
                    final_title.append(i)
                
                if i in always_lower:
                    i.lower()
                    final_title.append(i)
            final_title_output = " ".join(final_title)
            self.user_input = final_title_output

    def validate_country(self):
        """User inputs the country name and then check if users input is in the
        dataset. Call method check_input to fix any capltalization issues. 
        Iterate if country doesn't exist within dataset or incorrectly spelled.

            Args:
                user_input(str): country name the user inputs.

            Returns:
                print(str): Return the users input if the country name is 
                incorrectly spelled, or doesn't exist within the dataset.  
        
            Side effects:
                prints to stdout.
        """
        self.user_input = input("What country would you like to look at?")
        while True:
            self.check_input()# call method 
            if (self.user_input in self.df["Country"].values): 
                print(self.user_input)
                break
            else:
                self.user_input = input("Country does not exist, try again.\n"
                                    "What country would you like to look at?")


    def graph(self, graph):
        """Display a graph of a country's year factor influencing life expectancy. 
        Years range from 2000 to 2015 for each country.  
        
        Args:
            user_input(str): country name the user inputs.
            
        Returns:
            A graph of the regression betweeen year and life expectency.
        
        Side effects:
            outputs graph to stdout.
        """
        graph_df = self.df[self.df["Country"] == self.user_input]  
        sns.pairplot(graph_df, x_vars=[graph],y_vars=["Life expectancy "], kind='reg')
        plt.show()
        
    def calc_coefficient(self):
        """Calculate the coefficient (linear regression) for the specified 
        country. This will use the statsmodels.api module to show linear 
        regression model for each factor in the csv file. Results will include 
        respective p-values (values thata re less than 0.05 are considered 
        statistically significant).
        
        Args:
            user_input(str): country name the user inputs.
        
        Returns:
            a linear regression statistical model of each factor.
            
        Side effects:
                outputs table to stdout. 
        """
        calc_df = self.df[self.df["Country"] == self.user_input] 
        X=calc_df[["Year",'Polio','Total expenditure','Schooling',
                   'Income composition of resources',
                   'Alcohol', 'Diphtheria ', 'Adult Mortality', 'Population']]
        y=calc_df["Life expectancy "]
        model=st.OLS(y,X).fit()
        predictions=model.predict(X)
        print(model.summary())
 
def main(filepath):
    """Main function: Will call the class dframe and 
    functions outside of the class. 
    
    """
    graph_list = ["Year","Adult Mortality","Alcohol","Polio",
                  "Total expenditure","Diphtheria ","Population",
                  "Income composition of resources","Schooling"]
    execute = dframe(filepath)
    execute.read_dframe()
    for a in graph_list:
         execute.graph(a)
    execute.calc_coefficient()

def parse_args(arglist):
    """ Parse command-line arguements.

        Expect mandatory args:
            filepath: a path to CSV file.
    
        Args:
            arglist (list of str): arguments from command-line.
    
        Returns:
            namespace: parsed arguments as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help= "path to Life Expectancy CSV file")
    return parser.parse_args(arglist)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:]) 
    main(args.filepath)
