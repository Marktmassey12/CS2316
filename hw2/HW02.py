## NOTES:

# CS 2316 - Spring 2023 - HW02 
# HW02: This homework is due by Friday, February 3rd @ 11:59PM through Gradescope

# This homework is divided into three sections.
# Questions 1 and 2 MUST BE DONE IN ONE LINE
# Questions 3 and 4 require you to download the "cats.txt" file
# Questions 5 and 6 require you to download the "michelin.csv" file

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW02.py  - Your submission should be named exactly HW02.py

# cats.txt and michelin.csv must be located in the same folder as HW02.py in order for your
# code to run properly

import json, csv
from pprint import pprint

def character_gryffindor(character_list):
    """
    Question 1
    You are given a list of characters in Harry Potter.
    Imagine you are Minerva McGonagall, and you need to pick the students from your own house, which is Gryffindor, from the list.
    To do so ...

    - THIS MUST BE DONE IN ONE LINE
    - First, remove the duplicate names in the list provided
    - Then, remove the students that are not in Gryffindor
    - Finally, sort the list of students by their first name
    - Don't forget to return the resulting list of names!

    Args:
        character_list (list)
    Returns:
        list

    >>> character_gryffindor(["Scorpius Malfoy, Slytherin", "Harry Potter, Gryffindor", "Cedric Diggory, Hufflepuff", "Ronald Weasley, Gryffindor", "Luna Lovegood, Ravenclaw"])
    ['Harry Potter, Gryffindor', 'Ronald Weasley, Gryffindor']

    >>> character_gryffindor(["Hermione Granger, Gryffindor", "Hermione Granger, Gryffindor", "Cedric Diggory, Hufflepuff", "Sirius Black, Gryffindor", "James Potter, Gryffindor"])
    ['Hermione Granger, Gryffindor', 'James Potter, Gryffindor', 'Sirius Black, Gryffindor']

    """
    #[character_list.remove() for i in character_list() if i != "Gryffindor".lower()]
    #character_list = sorted(set(character_list))
    #char_list = sorted(character_list, key=lambda name: name.split(" ")[0].lower())
    return sorted(set([i for i in character_list if i.split(" ")[2] == 'Gryffindor']), key=lambda name: (name.split(" ")[0].lower()))


def character_dict(prof_dict):
    """
    Question 2
    - Given a dictionary that maps a character to a list of professors they want to talk to, return a dictionary with
    the value being the list sorted by the last letter in each professors' last name.
    - If two professors have the same last letter of their last name, sort by the first letter of their first name.
    - THIS MUST BE DONE IN ONE LINE

    Args:
        prof_dict (dict)
    Returns:
        dict

    >>> character_dict({"Harry": ["Albus Dumbledore", "Minerva McGonagall", "Severus Snape", "Rubeus Hagrid"], "Hermione": ["Remus Lupin", "Alastor Moody", "Horace Slughorn"]})
    {'Harry': ['Rubeus Hagrid', 'Albus Dumbledore', 'Severus Snape', 'Minerva McGonagall'], 'Hermione': ['Horace Slughorn', 'Remus Lupin', 'Alastor Moody']}

    >>> character_dict({"Scorpius": ["Severus Snape", "Dolores Umbridge", "Horace Slughorn"], "Neville": ["Cuthbert Binns", "Rubeus Hagrid", "Minerva McGonagall"]})
    {'Scorpius': ['Dolores Umbridge', 'Severus Snape', 'Horace Slughorn'], 'Neville': ['Rubeus Hagrid', 'Minerva McGonagall', 'Cuthbert Binns']}

    """
    return {a: sorted(b, key = lambda x: (x[-1], x[0])) for a,b in prof_dict.items()}


def txt_to_csv(input_file):
    """
    Question 3
    - cats.txt contains information about cat breeds and their various characteristics.
    - Read the cats.txt with FILE I/O.
    - These are TAB separated values
    - Use a list of lists to create a CSV file with the appropriate data WITHOUT WHITESPACE (remove \t) named "cleaned_cats.csv".
    - Exclude the "body_type" column
    - If a row has a length < 5, remove it.
    - For strings containing extra quotes, strip the extra quotes.
    - Return the list of lists.

    Args:
        input_file (cats.txt)
    Returns:
        List of lists

    Output:
    [['breed', 'type', 'coat_type', 'coat_pattern'],
    ['Abyssinian', 'Natural', 'Short', 'Ticked tabby'],
    ['Aegean', 'Natural', 'Semi-long', 'Multi-color'],
    ['American Bobtail', 'Mutation', 'Semi-long', 'All'],
    ['American Curl', 'Mutation', 'Semi-long', 'All'],
    ['American Ringtail', 'Mutation', 'Semi-long', 'All'],
    ['American Shorthair', 'Natural', 'Short', 'All'],
    ...
    ['Ukrainian Levkoy', 'Crossbreed between the Donskoy and Scottish Fold', 'Hairless', 'Solid gray'],
    ['York Chocolate', 'Natural', 'Long', 'Solid chocolate, solid lilac and solid taupe or any of these colors with white']]

    Length:
    96
    """
    alist = []
    with open("cats.txt") as f:
        data = f.readlines()
    for row in data:
        innerList = row.strip().split('\t')
        if len(innerList) >= 5:
            innerList = innerList[0:2] + innerList[3: ]
            alist.append([row.strip('"') for row in innerList])
    with open("cleaned_cats.csv", "w") as fout:
     writer = csv.writer(fout, lineterminator = "\n")
     writer.writerows(alist)

    return alist 





    

def write_to_json(alist, output_file):
    '''
    Question 4
    - Using the list of lists from question 3, create a dictionary of lists where each key in the dictionary is a coat type
    - Only use information from EVEN lines. Skip all odd lines.
    - Each value should be a DISTINCT LIST of the coressponding coat patterns that a cat breed can have
    - Write the dictionary to a JSON file with the name passed in as output_file.
    - Return the dictionary of lists

    Args:
        alist (list of lists from Q3)
    Returns:
        dictionary of lists

    Output:
        {'All': ['All'],
        'Hairless': ['All', 'Solid gray', 'Solid', 'Solid black roan'],
        'Hairless, velour, brush, or straight coat': ['All'],
         'Long': ['All',
                  'All but colorpoint',
                  'Ticked tabby',
                  'Solid white',
                  'Colorpoint, mitted, or bicolor',
                  'Solid, classic tabby, spotted tabby and ticked tabby',
                  'Colorpoint',
                  'Solid chocolate, solid lilac and solid taupe or any of these colors '
                  'with white'],
             ...
        'Short/long': ['All', 'Colorpoint'],
        'Short/long (longhair, sometimes in early generations, can appear to be semi-long)': ['All']}
    '''
    adict = {}
    llist = []
    for i in alist:
        llist = alist[2::2]
        for i in llist:
            if i[2] not in adict:
                adict[i[2]] = [i[3]]
            else:
                if i[3] not in adict[i[2]]:
                    adict[i[2]] += [i[3]]
    with open(output_file, "w") as output_file:
        json.dump(adict, output_file)
    return adict

def csv_cleaner(input_file):
    '''
    Question 5
    - Read michelin.csv with CSV module and return a list of lists containing each cleaned row.
        - Make sure to include the headers
    - There are 3 issues with the csv that must be fixed:
        1. Combine the last 2 columns to make one column. Rename this to be 'Cuisine Type'
        2. Remove any excess white space from the new column, 'Cuisine Type', as well as the column titled 'Country'
        3. Fill in all empty spaces in the 'Price' column with the average (as an integer) of the total price in an equivalent string format
            - 1 is equiavlent to $
            - 2 is equivalent to $$
            - 3 is equivalent to $$$ and so on
            - Average is equal to the total dollar signs / total number of rows
    - Write the list of lists to a new csv file called 'clean_michelin.csv' to use for Question 6
        - Make sure to write to the new csv file before the return statement

    Args:
        input_file(michelin.csv)
    Returns:
        Nested list

    Expected Output:
    [['',
      'Unnamed: 0',
      'Restaurant Name',
      'Number of Stars',
      'City',
      'Country',
      'Price',
      'Cuisine Type'],
    ...
     ['3325',
      '3325',
      'Bottiglieria 1881',
      '1',
      'Cracow',
      'Poland',
      '$$$',
      'Creative']]

    '''
    with open ("michelin.csv", 'r') as fin:
        readerObj = csv.reader(fin)
        info = [i for i in readerObj]

    for i in info:
        i[-2:] = [' '.join(i[-2:]).strip()]
        info[0][-1] = "Cuisine Type"
        i[-1] = i[-1].strip()
        i[-3] = i[-3].strip()


    prices = [i[-2] for i in info[1:]]

    aprice = sum(len(price) for price in prices) / len(prices)
    for i in info[1:]:    
        if i[-2] == " ":
            i[-2] = '$' * int(aprice)
        elif i[-2] == "":
            i[-2] = '$' * int(aprice)



    with open('clean_michelin.csv', 'w', newline='') as fout:
        newFile = csv.writer(fout)
        newFile.writerows(info)

    return info

def michelin_guide(input_file):
    """
    Question 6
    - You want to identify which types of cuisine are most
    popular in each country.
    - Using the output from question 5, create a dictionary
    mapping the countries to an inner dictionary.
    - The inner dictionary should map the "Cuisine Type"
    to the total number of that cuisine type in that country.
    - Return the dictionary.

    Args:
        input_file(clean_michelin.csv)
    Returns:
        Nested dictionary

    Expected Output:

    {'Andorra': {'Creative': 1},
     'Austria': {'Classic Cuisine': 1,
                 'Creative': 10,
                 'Japanese': 1,
                 'Modern Cuisine': 4,
                 'Vegetarian': 1},
     'Belgium': {'Asian': 1,
                 'Asian Influences': 1,
                 'Classic Cuisine': 8,
                 'Classic French': 4,
                 'Contemporary': 3,
                 'Country cooking': 1,
                 'Creative': 33,
                 'Creative French': 13,
                 'French': 2,
                 'French Contemporary': 3,
                 'Home Cooking': 1,
                 'Italian': 3,
                 'Italian Contemporary': 1, ...

    """
def michelin_guide(input_file):

    with open("clean_michelin.csv", 'r') as infile:
        reader_obj = csv.reader(infile) 
        data = [x for x in reader_obj] 
        finalDict={}

        for i in sorted(data, key=lambda data:data[-3]):
            if i[-3] not in finalDict.keys():
                iDict = {}
                iDict[i[-1]]=1
                finalDict[i[-3]]=iDict
            else:
                if i[-1] not in iDict.keys():
                    iDict[i[-1]]=1
                    finalDict[i[-3]]=iDict
                elif i[-1] in iDict.keys():
                    iDict[i[-1]]+=1
                    finalDict[i[-3]]=iDict

        Keys = list(finalDict.keys())
        Keys.sort()
        sorted_dict = {x: finalDict[x] for x in Keys}

        return sorted_dict



if __name__ == "__main__":
    ## Question 1
    print(character_gryffindor(["Scorpius Malfoy, Slytherin", "Harry Potter, Gryffindor", "Cedric Diggory, Hufflepuff", "Ronald Weasley, Gryffindor", "Luna Lovegood, Ravenclaw"]))
    print(character_gryffindor(["Hermione Granger, Gryffindor", "Hermione Granger, Gryffindor", "Cedric Diggory, Hufflepuff", "Sirius Black, Gryffindor", "James Potter, Gryffindor"]))

    ## Question 2
    print(character_dict({"Harry": ["Albus Dumbledore", "Minerva McGonagall", "Severus Snape", "Rubeus Hagrid"], "Hermione": ["Remus Lupin", "Alastor Moody", "Horace Slughorn"]}))
    print(character_dict({"Scorpius": ["Severus Snape", "Dolores Umbridge", "Horace Slughorn"], "Neville": ["Cuthbert Binns", "Rubeus Hagrid", "Minerva McGonagall"]}))

    ## Question 3
    print(txt_to_csv("cats.txt"))

    ## Question 4
    pprint(write_to_json(txt_to_csv("cats.txt"), 'cats.json'))

    ## Question 5
    pprint(csv_cleaner('michelin.csv'))

    ## Question 6
    pprint(michelin_guide("clean_michelin.csv"))

    pass



