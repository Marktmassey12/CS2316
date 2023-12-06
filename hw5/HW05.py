
import pandas as pd
from pprint import pprint

## NOTES:

# CS 2316 - Spring 2023 - HW05 Pandas
# HW05: This homework is due by Sunday, March 5th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW05.py  - Your submission should be named exactly HW05.py
#   - Print your variables as you code in order to see what values they have
#     especially for questions with API and BeautifulSoup

###################################################
###################################################
"""
DATA CLEANING SECTION
"""
###################################################
###################################################

def merge_columns(michelin_guide):
    """
    Question 1

    You have been provided with a dataframe containing the uncleaned data from the
    "michelin.xlsx" file. Your first task is to use pandas to merge the last
    two colums: "Cuisine_type_1" and "Cuisine_type_2" into one column
    titled "Cuisine Type". Follow the below rule

    - Fill all of the NaN values in "Cuisine_type_1" with the corresponding value in
      "Cuisine_type_2"
    - When finished you should create a new column titled "Cuisine Type", and drop
      the columns titled "Cuisine_type_1" and "Cuisine_type_2"

    You should modify the original dataframe rather than creating a new one

    NOTE: The output of this problem will be the input for the following problem

    Args:
        michelin_guide (pd.DataFrame)
    Returns:
        pd.DataFrame

    >>> merge_columns(michelin_guide)

                Restaurant Name  Number of Stars  ... Price     Cuisine_type
    0                  essência                1  ...   $$$   Modern Cuisine
    1                     Babel                1  ...  $$$$   Modern Cuisine
    2     Borkonyha Winekitchen                1  ...    $$   Modern Cuisine
    3                    Costes                1  ...  $$$$   Modern Cuisine
    4                     Stand                2  ...  $$$$   Modern Cuisine
    ...                     ...              ...  ...   ...              ...
    3321               Kan Suke                1  ...   NaN         Japanese
    3322                 Picchi                1  ...   NaN          Italian
    3323                    Oro                2  ...   NaN         Creative
    3324                  Lasai                1  ...   NaN   Modern Cuisine
    3325      Bottiglieria 1881                1  ...   $$$         Creative

    [3326 rows × 6 columns]
    """

    michelin_guide.Cuisine_type_1.fillna(michelin_guide.Cuisine_type_2, inplace = True)
    del michelin_guide['Cuisine_type_2']
    michelin_guide.rename(columns={'Cuisine_type_1': 'Cuisine Type'}, inplace=True)
    return michelin_guide


def price_cleaning(michelin_guide):
    """
    Question 2

    Using the cleaned michelin guide dataframe from above you will replace the NaN
    values in the "Price" column with the number of "$" corresponding to the
    average number of dollar signs of the whole column

    Outline of steps below:

    - Find the average number of dollar signs in each of the cells.
      Hint: Use df.str with .len() and .mean()

    - Once you have found the average number cast it to an integer and multiply
      it by the dollar sign

    - Fill in any NaN values in the column with the value found above

    You should modify the original dataframe rather than creating a new one

    NOTE: The output of this problem will be the input for the following problem

    Args:
        michelin_guide (pd.DataFrame)

    Returns:
        pd.DataFrame

    >>> price_cleaning(michelin_guide)

                Restaurant Name  Number of Stars  ... Price     Cuisine type
    0                  essência                1  ...   $$$   Modern Cuisine
    1                     Babel                1  ...  $$$$   Modern Cuisine
    2     Borkonyha Winekitchen                1  ...    $$   Modern Cuisine
    3                    Costes                1  ...  $$$$   Modern Cuisine
    4                     Stand                2  ...  $$$$   Modern Cuisine
    ...                     ...              ...  ...   ...              ...
    3321               Kan Suke                1  ...   $$$         Japanese
    3322                 Picchi                1  ...   $$$          Italian
    3323                    Oro                2  ...   $$$         Creative
    3324                  Lasai                1  ...   $$$   Modern Cuisine
    3325      Bottiglieria 1881                1  ...   $$$         Creative

    [3326 rows x 6 columns]

    """
    avg = michelin_guide['Price'].str.len().mean()
    avge = (int(avg)*'$')
    michelin_guide.Price.fillna(avge, inplace = True)
    return michelin_guide
    


def write_to_file(michelin_guide, output_file, sheet):
    '''
    Question 3

    Write the michelin_guide dataframe to an excel file and rename the sheet
    according to the sheet parameter. The file name is provided as the
    output_file parameter. Make sure you do not include the index column when you
    write it to the file

    This must be done in one line

    The data in this file will be used in questions 4-7

    Args:
        michelin_guide (pd.DataFrame)
        output_file (str)
        sheet (str)

    Returns:
        None

    >>> write_to_file(michelin_guide, "cleaned_guide.xlsx", "michelin_guide")
        None

    '''
    return michelin_guide.to_excel(output_file, sheet_name = sheet, index = False)
    


###################################################
###################################################
"""
DATA ANALYSIS SECTION
"""
###################################################
###################################################


def types_by_country(michelin_guide):
    """
    Question 4

    Return a dataframe that gives the number of restaurants by Cuisine Type for
    each country. You will need to use .groupby and .agg

    This must be done in one line

    Args:
        michelin_guide (pd.DataFrame)

    Returns:
        pd.DataFrame

    >>> types_by_country(michelin_guide)

                                        Restaurant Name
    Country        Cuisine Type
    Andorra        Creative                           1
    Austria        Classic Cuisine                    1
                   Creative                          10
                   Japanese                           1
                   Modern Cuisine                     4
    ...                                             ...
    United Kingdom Modern French                      3
                   Scandinavian                       1
                   Seafood                            5
                   Spanish                            3
                   Traditional British                5

    [413 rows x 1 columns]

    """
    return michelin_guide.groupby(["Country", "Cuisine Type"]).aggregate({"Restaurant Name": "count"})
    


def best_cities(michelin_guide, country, cuisine_type):
    """
    Question 5


    Given a country and a cuisine type, find the maximum rating (most Michelin stars)
    among restaurants serving that cuisine type in the country and return the number
    of distinct cities in this country that have at least one restaurant of the specified
    cuisine type with this maximum rating.

    Args:
        michelin_guide (pd.DataFrame)
        country (str)
        cuisine_type (str)

    Returns:
        int

    >>> best_cities(michelin_guide, "France", "Seafood")
    2
    >>> best_cities(michelin_guide, "USA", "Korean")
    1
    """
    bCountry = michelin_guide.loc[:, "Country"] == country 
    bCuisuine = michelin_guide.loc[:, "Cuisine Type"] == cuisine_type
    distinct = michelin_guide[bCuisuine][bCountry]
    maxim = distinct.loc[:, "Number of Stars"] == distinct.loc[:, "Number of Stars"].max()
    return distinct[maxim].City.unique().size



def food_budget(michelin_guide, price_threshold, city):
    """
    Question 6

    Given a price threshold and a city name, return a dataframe that includes the
    number of restaurants for each cuisine type in that city having a price value
    at or below the specified threshold.

    Args:
        michelin_guide (pd.DataFrame)
        price_threshold (str)
        city (str)

    Return:
        pd.DataFrame

    >>> food_budget(michelin_guide, "$$$", "Rio de Janeiro")

                          Restaurant Name
    Cuisine Type
    Asian Influences                1
    Creative                        1
    Italian                         1
    Modern Cuisine                  2

    >>> food_budget(michelin_guide, "$$", "Taipei")

                          Restaurant Name
    Cuisine Type
    Taiwanese                       3

    """
    df = michelin_guide
    dfa = df.copy()
    dfa.loc[:,"Price_int"] = dfa["Price"].str.len()
    dfb = dfa[(dfa["City"] == city) & (dfa["Price_int"].astype("int64") <= len(price_threshold))].groupby("Cuisine Type").agg({"Restaurant Name":"count"})
    return dfb
    


def ranking_restaurants(michelin_guide, cuisine_type, price):
    """
    Question 7

    Given a cuisine type and a price bracket, return a Dataframe of
    all restaurants serving that cuisine type within that price bracket.
    Sort the restaurants from lowest to highest star rating followed by the Country.
    Change the indicies, so they remain in ascending order. Please only return
    the "Restaurant Name", "Number of Stars", and "Country" columns


    Args:
        michelin_guide (pd.DataFrame)
        cuisine_type (str)
        price (str)

    Return:
        pd.DataFrame

    >>> ranking_restaurants(cleaned_guide, "Modern Cuisine", "$$$")

             Restaurant Name  Number of Stars         Country
    0       The Glass Garden                1         Austria
    1          Chai Gourmand                1         Belgium
    2                Vintage                1         Belgium
    3               Quai n°4                1         Belgium
    4                    JER                1         Belgium
    ..                   ...              ...             ...
    435             Portland                1  United Kingdom
    436              Trinity                1  United Kingdom
    437  Konstantin Filippou                2         Austria
    438               Oteque                2          Brazil
    439            La Brezza                2     Switzerland

    [440 rows x 3 columns]


    >>> ranking_restaurants(cleaned_guide, "Creative", "$$$$")

              Restaurant Name  Number of Stars         Country
    0                   Ibaya                1         Andorra
    1            Kilian Stuba                1         Austria
    2                   APRON                1         Austria
    3      Pramerl & the Wolf                1         Austria
    4     La Villa in the Sky                1         Belgium
    ..                    ...              ...             ...
    473                  ABaC                3           Spain
    474              Memories                3     Switzerland
    475  Schloss Schauenstein                3     Switzerland
    476             L'Enclume                3  United Kingdom
    477              Fat Duck                3  United Kingdom

    [478 rows x 3 columns]

    """
    df = michelin_guide
    dfa = df[(df["Cuisine Type"] == cuisine_type) & (df["Price"] == price)]
    dfb = dfa.drop(["City", "Price", "Cuisine Type"], axis = 1)
    dfb.sort_values(["Number of Stars", "Country"], ascending = [True, True], inplace = True)
    dfb.reset_index(drop = True, inplace = True)
    return dfb


def mean_cuisine(michelin_guide, rating):
    """
    Question 8

    Given a rating, return a Series with all cuisine types
    with a mean star rating above the given star rating. Please
    round the mean rating to two decimal places.

    Args:
        michelin_guide (pd.DataFrame)
        rating (int)

    Return:
        pd.Series

    >>> mean_cuisine(cleaned_guide, 1.2)

                         Cuisine Type
    American                     1.38
    Asian                        1.38
    ...
    Taizhou                      1.50
    Tempura                      1.22

    [28 rows x 1 columns]


    >>> mean_cuisine(cleaned_guide, 1.4)

                         Cuisine Type
    Asian Contemporary           1.50
    Classic French               1.42
    ...
    Southern Thai                2.00
    Taizhou                      1.50

    [9 rows x 1 columns]

    """
    #ser = michelin_guide.iloc[;,"Cuisine Type", "Number of Stars"].means()
    # df2 = michelin_guide[["Cuisine Type", "Number of Stars"]].mean(axis = 1)
    # series = michelin_guide.Series(data["Cuisine Type", "Number of Stars"], index = data.index)
    # series[series > rating]
    # return series
    df = michelin_guide
    dfa = df.copy()
    dfb = dfa.groupby("Cuisine Type").agg({"Number of Stars":"mean"})
    dfc = dfb[dfb["Number of Stars"] > rating].round(2)
    ser = dfc.iloc[:,0]
    return ser
    


if __name__ == "__main__":

    # # Q1
    michelin_guide = pd.read_excel("michelin.xlsx")
    pprint(merge_columns(michelin_guide))

    # # Q2
    michelin_guide = pd.read_excel("michelin.xlsx")
    merge_columns(michelin_guide)
    pprint(price_cleaning(michelin_guide))

    # Q3
    michelin_guide = pd.read_excel("michelin.xlsx")
    merge_columns(michelin_guide)
    price_cleaning(michelin_guide)
    write_to_file(michelin_guide, "cleaned_guide.xlsx", "michelin_guide")

    ####################################################
    ####################################################
    """
    DO NOT MODIFY CODE BELOW
    """
    try:
        cleaned_guide = pd.read_excel("cleaned_guide.xlsx")
    except:
        print("##########\n#\nYou must complete questions 1-3 before moving on to questions 4-7\n#\n##########")

    ####################################################
    ####################################################

    # Q4
    pprint(types_by_country(cleaned_guide))

    # Q5
    pprint(best_cities(cleaned_guide, "France", "Seafood"))
    pprint(best_cities(cleaned_guide, "USA", "Korean"))

    # # Q6
    pprint(food_budget(cleaned_guide, "$$$", "Rio de Janeiro"))
    pprint(food_budget(cleaned_guide, "$$", "Taipei"))

    # Q7
    pprint(ranking_restaurants(cleaned_guide, "Modern Cuisine", "$$$"))
    pprint(ranking_restaurants(cleaned_guide, "Creative", "$$$$"))

    # Q8
    pprint(mean_cuisine(cleaned_guide, 1.2))
    pprint(mean_cuisine(cleaned_guide, 1.4))







