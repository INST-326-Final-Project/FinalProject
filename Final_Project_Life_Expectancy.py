"""
Script takes the users input and outputs information & data on a country. 
"""
#Import necessary modules.
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
    
    def __init__(self, filepath, user_input=0):
        """ User inputs the country name. Will include each row with the country
        name and for each year it shows up for.

            Args:
                user_input(str): country name the user inputs.
                df (str): dataframe of the file
                
            Returns:
                user_input(str): name of the country
        """
        self.user_input = user_input
        self.user_input = input("What country would you like to look at? ")
        self.df = pd.read_csv(filepath)
        
    
    def read_dframe(self):
        """Method that reads in the "cleaned_life_expectancydf.csv" file and 
        creates a dataframe with pandas based on the dataset.
                
            Returns:
                  dataframe: dataframe of the csv file. This dataframe contains 
                193 country names, alongside their associated factors. This is 
                a requirement to run the file. 
        """
        
        # prints the 15 rows from the dataframe for that country
        output = print(self.df[self.df["Country"] == self.user_input])
        
        return output
    
    def check_input(self):
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
        
        final_title = []
        always_lower = ["in", "and", "of", "former", "the"]
        
        if (self.user_input in self.df["Country"].values):
            print("yes")
    
        elif (self.user_input not in self.df["Country"].values):
            lower = self.user_input.lower()
            templist = lower.split(" ")
            
            for i in templist:
                if i not in always_lower:
                    i = i.title()
                    final_title.append(i)
                
                if i in always_lower:
                    i.lower()
                    final_title.append(i)
            final_title_output = " ".join(final_title)
            print(final_title_output)
        
        

    def year(self):
        """Display a graph of a country's year factor influencing life 
        expectancy. 
        Years range from 2000 to 2015 for each country.  
    
        Args:
            user_input(str): country name the user inputs.
        
        Returns:
            A graph of the regression betweeen year and life expectency.
    
        Side effects:
            outputs graph to stdout.
        """
        year_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(year_df, x_vars = ["Year"], y_vars = ["Life expectancy "], 
                     kind = "reg")
        plt.show()

    def polio(self):
        """Display a graph of a country's polio factor influencing 
        life expectancy.
        Polio (Pol3) immunization coverage among 1-year-old infants.
    
        Args:
            user_input(str): country name the user inputs.
    
        Returns:
            A graph of the regression betweeen polio immunization and life 
            expectency.
        
        Side effects:
            outputs graph to stdout.
        """
        polio_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(polio_df, x_vars = ["Polio"], y_vars = ["Life expectancy "],
                     kind = "reg")
        plt.show()

    def total_exp(self):
        """Display a graph of a country's total expenditure factor influencing 
        life expectancy. General government expenditure on health as a 
        percentage of total government expenditure. 
    
        Args:
            user_input(str): country name the user inputs.
    
        Returns:
            A graph of the regression betweeen governmnet expenditure and life 
            expectency.
        
        Side effects:
            outputs graph to stdout.
        """
        total_exp_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(total_exp_df, x_vars = ["Total expenditure"], y_vars = 
                     ["Life expectancy "], kind = "reg")
        plt.show()
    
    def schooling(self):
        """Display a graph of a country's schooling factor influencing life 
         expectancy.
        
        Args:
         user_input(string): The country that schooling will be analyzed and 
            derived from
    
        Returns:
            A graph of the regression betweeen schooling and life expectency.
        
        Side effects:
            outputs graph to stdout.
        """
        schooling_df = self.df[self.df["Country"] == self.user_input] 
        sns.pairplot(schooling_df, x_vars = ["Schooling"], 
                     y_vars = ["Life expectancy "], kind = "reg")
        plt.show()

    def income_comp(self):
        """Display a graph of a country's Income composition of resources factor 
        influencing life expectancy.

        Args:
            user_input(string): The country that the income_comp will be derived 
            from
    
        Returns:
            A graph of the regression between income_comp and life expectency.
        
        Side effects:
            Outputs graph to stdout.
     """
        income_comp_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(income_comp_df, x_vars = ["Income composition of resources"], 
                     y_vars = ["Life expectancy "], kind = "reg")
        plt.show()
        
    def alcohol(self):
        """Display a graph of a country's alcohol consumption factor influencing 
        life expectancy. Will analyze the affect of this factor on the 
        independent variable
    
        Args:
            user_input(str): The name of the country that this is being 
            analyzed on
    
        Returns:
            A graph of the regression between alcohol and life expectency.
    
        Side effects:
            outputs graph to stdout.
        """ 
        alcohol_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(alcohol_df, x_vars = ["Alcohol"], y_vars = 
                     ["Life expectancy "], kind = "reg")
        plt.show()
        
    def diphtheria(self):
        """Display a graph of a country's diphtheria factor influencing life 
        expectancy. Shows the factor of Diptheria tatnus toxoid & pertussis 
        (DTP3) immunization amongst young children (1-year olds).
            
        Args:
            user_input(str): country name the user inputs.
        
        Returns:
            A graph of the regression between diphtheria and life expectency.
            
        Side effects:
                outputs graph to stdout.
        """ 
        dip_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(dip_df, x_vars=["Diphtheria "],y_vars=["Life expectancy "], 
                     kind='reg')
        plt.show()

    def adult_mortality(self):
        """Display a graph of a country's adult mortality factor influencing 
        life expectancy. Adult mortality rates are presented as the probablility 
        of dying between the ages of 15 to 60 per 1000 population. 
        
        Args:
            user_input(str): country name the user inputs.
        Returns:
            A graph of the regression between adult_mortality and life 
            expectency.
            
        Side effects:
                outputs graph to stdout.
        """ 
        am_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(am_df, x_vars=["Adult Mortality"],
                     y_vars=["Life expectancy "], kind='reg')
        plt.show()
    
    def population(self):
        """Display a graph of a country's population factor influencing life 
        expectancy. Populations range within the million to tens of millions. 
        
        Args:
            user_input(str): country name the user inputs.
        
        Returns:
            A graph of the regression between population and life expectency.
            
        Side effects:
                outputs graph to stdout.
        """
        pop_df = self.df[self.df["Country"] == self.user_input]
        sns.pairplot(pop_df, x_vars=["Population"],y_vars=["Life expectancy "], 
                     kind='reg')
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
    execute = dframe(filepath, user_input=0)
    execute.read_dframe()
    execute.check_input()
    execute.year()
    execute.polio()
    execute.total_exp()
    execute.schooling()
    execute.income_comp()
    execute.alcohol()
    execute.diphtheria()
    execute.adult_mortality()
    execute.population()
    execute.calc_coefficient()
    
if __name__ == "__main__":
    main(sys.argv[1])
