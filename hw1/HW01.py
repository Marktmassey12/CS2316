
## NOTES:

# CS 2316 - Spring 2023 - HW01 Python Fundamentals
# HW01: This homework is due by Wednesday, January 25th @ 11:59PM through Gradescope
# HW00: Installation Verification is also due by Monday, January 23rd @ 11:59PM through Canvas

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW01.py  - Your submission should be named exactly HW01.py

## Optional: All of these problems can be completed in one line. This is not required, but it is
##           good practice for the exam

def welcome_class():
    """
    Question 0
    Print the exact string, "Welcome to CS2316!"

    NOTE: This must be done in one line

    >>> welcome_class()
    'Welcome to CS2316!'
    """
    print("Welcome to CS2316!")

def where_to(message):
    """
    Question 1
    Your friend wants to meet you somewhere on Tech campus, but somehow
    their message was corrupted, and numbers have been added to their message!
    Return the message with all of the numbers removed.
    Args:
        message (str)
    Returns:
        str

    >>> where_to("Le1t's5 me8et0 a777t Ken4d6eda!")
    'Let's meet at Kendeda!'

    >>> where_to("Ho0w a2bo8ut ha8vin2g 3lun2ch7 a3t W99ill0age?")
    'How about having lunch at Willage??'

    """
    result = ''.join(i for i in message if not i.isdigit())
    return result
    
    

def name_sort(staff):
    '''
    Question 2
    You are given a list of Georgia Tech staff members- each with a first and last name separated by a space,
    and need to sort them alphabetically by last name for a directory. However, the person who provided you the list
    did not proofread the records and accidentally misspelled some of the names. You can identify which ones
    have typos just by looking at the first letter of the first name.

        - First, sort the list alphabetically by the last name.
        - Remove any members whose first name starts with "Q" or "X".
        - Return the resulting list.

    Args:
        staff (list)
    Returns:
        list

    >>> name_sort(['Damon Williams', 'Xngel Cabrera', 'George Burdell', 'Brett Key', 'David Joyner', 'Qon Lowe'])
        ['George Burdell', 'David Joyner', 'Brett Key', 'Damon Williams']

    '''
    staff.sort(key = lambda x: x.split()[-1])
    staff = [i for i in staff if not i.startswith("Q")]
    staff = [i for i in staff if not i.startswith("X")]
    return staff
    print(staff)

    
  
    

def gpa_manipulation(gpa_list):
    '''
    Question 3
    You are working in the registrars office and have a been given a list of the average gpas of
    each of the colleges at Georgia Tech: Scheller, College of Engineering, College of Design,
    College of Computing, Ivan Allen, College of Sciences.

    NOTE: GPA's are made up and in no particular order

    - First, one of the GPA's is None. Replace None with
      the 3.80.

    - Second, reverse the order of the list you are given.
      This should not be sorted simply reversed from the way
      you were given them

    - Third, change the type of the list to a tuple

    Args:
        gpa_list (list)
    Returns:
        tuple

    >>> gpa_manipulation([3.72, 3.25, 3.43, 2.99, None, 3.87])
        (3.87, 3.80, 2.99, 3.43, 3.25, 3.72)

    '''
    gpa_list = [3.80 if i is None else i for i in gpa_list]
    gpa_list.reverse()
    return tuple(gpa_list)

    
    
    

def motto_maker(slogan1, slogan2):
    '''
    Question 4
    You are asked to write a slogan generator that creates new slogans out of
    existing Georgia Tech mottos slogan1 and slogan2. Your returned result
    should be:
    "From 'slogan1' and 'slogan2' comes 'slogan1' 'slogan2'. How does that sound?"

    Note: You must use f-string to do this question.

    Args:
        slogan1 (str), slogan2 (str)
    Returns:
        string

    >>> motto_maker("Put in", "a Ramblin' Wreck from Georgia Tech")
        "From 'Put in' and ' a Ramblin' Wreck from Georgia Tech' comes 'Put in a Ramblin' Wreck from Georgia Tech'. How does that sound?"

    '''
    return f"From '{slogan1}' and '{slogan2}' comes '{slogan1} {slogan2}'. How does that sound?"

def engineering_types(majors):
    '''
    Question 5
    You are teaching Calculus at Georgia Tech and want to know what engineering majors are represented in your class
    based on survey responses.

    - Remove any non-engineering majors from the list
    (in other words, the ones that do not explicitly have "engineering" as the second word)
        Hint: The word "engineering" may be capitalized in some cases but not in others.
        Use .lower() or .upper() to check this condition.
    - Return a list of distinct engineering disciplines present in the list sorted alphabetically.

    Args:
        majors (list)
    Returns:
        list

    >>> engineering_types(['Electrical engineering', 'Industrial engineering', 'Computer Science', 'Aerospace engineering',
                           'Industrial Engineering', 'Chemical Engineering', "International affairs", 'Aerospace Engineering'])
        ['Aerospace', 'Chemical', 'Electrical', 'Industrial']

    '''
    majors = set([i.split()[0] for i in majors if "engineering" in i.lower()])
    return sorted(majors)
    
    

def traditions_dict(adict):
    """
    Question 6
    Given a dictionary that maps a person to a list of their favorite
    GT traditions, return a dictionary with the value being
    the list sorted by the last letter of each tradition. If two
    traditions have the same last letter, sort by the first letter.

    HINT: This will require the use of lambda functions

    Args:
        adict (dict)
    Returns:
        dict

    >>> traditions_dict({"Jacob": ["The Horse", "Stealing the t", "Midnight Bud"],
                   "Athena": ["Mini Five-Hundred", "Freshman Cake Race", "Buzzweiser Song"],
                   "Liv": ["Freshman Cake Race", "George P. Burdell", "Buzzweiser Song"]})

    {'Jacob': ['Midnight Bud', 'The Horse', 'Stealing the t'],
    'Athena': ['Mini Five-Hundred', 'Freshman Cake Race', 'Buzzweiser Song'],
    'Liv': ['Freshman Cake Race', 'Buzzweiser Song', 'George P. Burdell']}

    >>> traditions_dict({"Madison": ["The Horse", "Midnight Bud", "Buzzweiser Song"],
                   "Anna": ["Mini Five-Hundred", "Buzzweiser Song", "Freshman Cake Race"],
                   "Ashok": ["The Horse", "Freshman Cake Race", "Stealing the t", "Midnight Bud"]})

    {'Madison': ['Midnight Bud', 'The Horse', 'Buzzweiser Song'],
    'Anna': ['Mini Five-Hundred', 'Freshman Cake Race', 'Buzzweiser Song'],
    'Ashok': ['Midnight Bud', 'Freshman Cake Race', 'The Horse', 'Stealing the t']}

    """
    dc = {a: sorted(b, key = lambda x: (x[-1], x[0])) for a,b in adict.items()}
    return dc

    
    

def classes(adict, major):
    """
    Question 7
    - Given a dict that maps a class number to a major identifiers
      where you could find that class number, return the set of numbers that
      one could take for a specific major!

    - For an extra challenge, try doing this in one line (Optional).

    Args:
        adict (dict)
        major (str)
    Returns:
        set

    >>> classes_dict = {4232: ["ISYE", "MATH", "HTS"],
                         2316: ["CS", "CX", "MGT"],
                         3000: ["ISYE", "MGT", "ECE"],
                         2027: ["ISYE", "PSYC", "HTS"]}

    >>> classes(classes_dict, "ISYE")
    {4232, 2027, 3000}

    >>> classes(classes_dict, "CS")
    {2316}

    """
    return set([i for i, v in adict.items() if major in v])

    
    #adict.items()
    #for key, value in adict.items():
        #if major == value
       # return key 
    
    #adict = {1: "a", 2: "b"}
    #adict.keys()
   # adict.values()
    #adict.items()
    #[(1, "a"), (2, "b")]


if __name__ == "__main__": #autograder ignores this

    # # Q0
    welcome_class()
    print('---')

    # # Q1
    # print(where_to("Le1t's5 me8et0 a777t Ken4d6eda!"))
    # print(where_to("Ho0w a2bo8ut ha8vin2g 3lun2ch7 a3t W99ill0age?"))
    # print('---')

    # # Q2
    # print(name_sort(['Damon Williams', 'Xngel Cabrera', 'George Burdell', 'Brett Key', 'David Joyner', 'Qon Lowe']))
    # print(name_sort(['Melinda McDaniel', 'Buzz Yellowjacket', 'Josh Pastner', 'Nell Fortner', 'Michelle Collier']))
    # print('---')

    # # Q3
    print(gpa_manipulation([3.72, 3.25, 3.43, 2.99, None, 3.87]))
    print(gpa_manipulation([3.11, 3.23, None, 3.97, 2.47, 3.36]))
    print('---')

    # # Q4
    print(motto_maker("Put in", " a Ramblin' Wreck from Georgia Tech"))
    print('---')

    # # Q5
    print(engineering_types(['Electrical engineering', 'Industrial engineering', 'Computer Science', 'Aerospace engineering', 'Industrial Engineering', 'Chemical Engineering', "International affairs", 'Aerospace Engineering']))
    print('---')

    # # Q6
    print(traditions_dict({"Jacob": ["The Horse", "Stealing the t", "Midnight Bud"], "Athena": ["Mini Five-Hundred", "Freshman Cake Race", "Buzzweiser Song"], "Liv": ["Freshman Cake Race", "George P. Burdell", "Buzzweiser Song"]}))
    print(traditions_dict({"Madison": ["The Horse", "Midnight Bud", "Buzzweiser Song"], "Anna": ["Mini Five-Hundred", "Buzzweiser Song", "Freshman Cake Race"],"Ashok": ["The Horse", "Freshman Cake Race", "Stealing the t", "Midnight Bud"]}))
    print('---')

    # # Q7
    classes_dict = {4232: ["ISYE", "MATH", "HTS"], 2316: ["CS", "CX", "MGT"], 3000: ["ISYE", "MGT", "ECE"], 2027: ["ISYE", "PSYC", "HTS"]}

    print(classes(classes_dict, "ISYE"))
    print(classes(classes_dict, "CS"))
    print('---')

    pass



