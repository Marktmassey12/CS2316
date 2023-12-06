## Notes:

# CS 2316 - Spring 2023 - HW04 Numpy
# HW04: This homework is due by Sunday, February 26th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW04.py  - Your submission should be named exactly HW04.py

import numpy as np
import random

def shopping_spree(spending_limit, store_nums):
    """
    QUESTION 1
    - You and your friends decide to go on a shopping spree! You each have a spending
      limit listed in a 1D array called spending_limit. 
    - You each know you will be going to a specific number of stores, store_nums, which is also
      a 1D array.
    - Sales tax is 7% at every store.
    - Calculate the average amount that you and each of your friends can spend at a store
    - Excluding sales tax from this calculation.
    - Return an array of how much you can each spend at a store, excluding sales tax.
    - THIS MUST BE DONE IN ONE LINE

    Args:
        spending_limit (np.array)
        store_nums (np.array)
    Returns:
        np.array

    >>  store_nums = np.array([15, 12, 8, 3, 4, 3, 6, 5, 7, 4])
        spending_limit = np.array([200, 500, 330, 120, 85, 60, 220, 190, 490, 300])

    >> print(shopping_spree(spending_limit, store_nums))
    [12.46105919 38.94080997 38.55140187 37.38317757 19.85981308 18.69158879
     34.26791277 35.51401869 65.42056075 70.09345794]

    """
    #get the average first then exclude sales tax
    #return np.subtract(spending_limit, spending_limit * .07) / store_nums
    return spending_limit / store_nums / 1.07


def serial_numbers(num_players):
    """
    QUESTION 2
    - You are going to assign each player a serial number in the game.
    - In order to make the players feel that the game is very popular with a large player base,
      you don't want the serial numbers to be consecutive.
    - Instead, the serial numbers of the players must be equally spaced, starting from 1 and going all the way up to 100 (inclusive).
    - Given the number of players in the system, return a 1D numpy array of the serial numbers for the players.
    - THIS MUST BE DONE IN ONE LINE

    Args:
        num_players (int)
    Returns:
        np.array

    >> serial_numbers(10)
    array([1. 12. 23. 34. 45. 56. 67. 78. 89. 100.])

    >> serial_numbers(12)
    array([1. 10. 19. 28. 37. 46. 55. 64. 73. 82. 91. 100.])

    """
    return np.linspace(1, 100, num=num_players,endpoint=True, dtype=float)

def bath_and_body(price_arr):
    '''
    QUESTION 3
    Right before checking out at Bath & Body Works, you take a quick inventory of
    your shopping cart. The number of candles and soaps you've accrued is embarrasing.
    You decide to put the most expensive item back on the shelf. Given the
    price of each item in your shopping cart, calculate the total cost of the items,
    excluding the most expensive item.

    THIS MUST BE DONE IN ONE LINE

    Args:
        price_arr(np.array)

    Return:
        float64

    >>> price_arr1 = np.array([10.25, 12.5, 5.25, 29.5, 2.5], dtype = "float64")

    >>> bath_and_body(price_arr1)
    30.5
    '''
    # print(price_arr[price_arr < price_arr.max()])
    return np.sum((price_arr[price_arr < price_arr.max()]), dtype = float)

def shoe_shopping(shoe_arr):
    '''
    QUESTION 4
    You're shopping on a budget and want to determine the cheapest shoe brand
    given an array of brands and prices. Return the brand with the lowest
    average price.

    Hint: You should create a new array of the prices with the correct dtype.

    Args:
        shoe_list(np.arry)

    Return:
        string

    >>> shoe_list1 = np.array([["Nike", "Adidas", "New Balance"],
                             ["110.99", "135.99", "94.99"],
                             ["85.99", "150.99", "105.99"],
                             ["225.99", "145.99", "130.99"]])

    >>> shoe_shopping(shoe_list1)
    'New Balance'
    '''
    brands = np.array(shoe_arr[1:, :], dtype = float)
    brandsMean = np.mean(brands, axis=0)
    #print(brands.min()) #use this as a mask
    cheapestBrand = np.array(shoe_arr[0,:])
    #print(cheapestBrand)
    minimum = brandsMean[0]
    minIndex = 0
    for i in range(len(brandsMean)):
        if(i < minimum):
            minIndex = i
    return np.array((cheapestBrand[minIndex]))
    #return np.array((cheapestBrand[brands.min()]), dtype = str)


def coupons(my_list, on_sale, prices):
    '''
    QUESTION 5
    It's the time of week to go grocery shopping again!
    Given three arrays, one of what's on sale, one of your own list, and one of the prices, return an array of the items on your list that are
    on sale and more than five dollars. You have MORE coupons than you have groceries on your list- make sure to only use the coupons
    that correspond to your list.

    THIS MUST BE DONE IN ONE LINE
    Hint: use masking and slicing

    Args:
        my_list(np.array)
        on_sale(np.array)
        prices(np.array)

    Return:
        np.array

    >>> my_list = np.array(["eggs", "2% milk", "green onions", "whole wheat bread",
                            "onions", "spinach", "peanut butter", "boxed spaghetti",
                            "salt and vinegar chips", "alfredo sauce"])
    >>> on_sale = np.array([True, False, True, True, True, True, False, False, False, True, False, True, False])
    >>> prices = np.array([5.13, 4.29, 1.99, 5.19, 8.99, 3.50, 6.79, 2.19, 3.49, 2.09])

    >> coupons(tracks, ratings)
    ['eggs' 'whole wheat bread' 'onions']
    '''
    return np.array(my_list[(on_sale[0:len(my_list)] & (prices > 5))])

def missing_bags(week1, week2, start_day, stop_day):
    '''
    QUESTION 6
    You are managing the candy aisle, specifically the Jolly Ranchers. Your manager wants you to track
    how many there are on the shelves over the course of two weeks- here's the thing, you accidentally misplaced 4 bags of the candy,
    and you need to send in the real report of the days that were incorrect (+4 to the relevant days).

    You misplace the bags on the start day and return them back on the stop day (stop is inclusive). Day 0 is index 0
    Using the two arrays given, write a function in ONE LINE that returns the incorrect days with their values changed.

    The starting index is 0 for day 0.

    hint: use concatenate

    Args:
        week1(np.array)
        week2(np.array)
        start_day(int)
        stop_day(int)

    Return:
        np.array

    >>> week1 = np.array([27, 25, 25, 24, 24, 24, 20])
    >>> week2 = np.array([19, 18, 14, 11, 7, 5, 4])
    >>> start_day = 6
    >>> stop_day = 13

    >> missing_bags(week1, week2, start_day, stop_day)
    [24 23 22 18 15 11  9  8]
    '''
    #return np.concatenate(week1,week2, axis = None) #concatenates week one and two 
    #return np.concatenate((week1[start_day], week2[stop_day]), axis = None) #maybe try linspace 
    return np.concatenate((week1, week2), axis = None)[start_day:stop_day+1]+4
    #return np.arange(start_day, stop_day) #only returns the indices. Not data values. 

    

def purchases(transactions):
    """
    QUESTION 7
    - A high-end store is trying to evaluate the total amount that customer's spend per transaction. They
      want customers to spend anywhere between $130 and $150 on average.
    - You need to determine whether the average number spent on each transaction per month is above, between, or
      below the desired amount.
    - Transactions is a numpy array containing a date, total amount earned each month, and total
      number of transactions each month.
    - Above: month's average amount spent per transaction > 150
    - Within Range: 150 >= month's average amount spent per transaction >= 130
    - Below: month's average amount spent per transaction < 130
    - Return a numpy array with "Above", "Within Range" and "Below" for the average amount spent per transaction per month
    - THIS MUST BE DONE IN ONE LINE
    HINT: use np.where() and convert the type of each column to float

    Args:
        transactions (np.array)
    Returns:
        np.array

    >> transactions = np.array([['01-31-2022', 5462101, 24752],
        ['02-28-2022', 7081547.30, 34615],
        ['03-31-2022', 3287654.57, 16588],
        ['04-30-2022', 8725851.81, 45621],
        ['05-31-2022', 6730748.72, 26741],
        ['06-30-2022', 9562745.43, 76436],
        ['07-31-2022', 8641735.21, 61448],
        ['08-31-2022', 7641748.57, 52846],
        ['09-30-2022', 7645277.02, 65457],
        ['10-31-2022', 9416274.67, 65109],
        ['11-30-2022', 9841378.97, 57254],
        ['12-31-2022', 10654298.18, 98651]])

    >> purchases(transactions)
        ['Above' 'Above' 'Above' 'Above' 'Above' 'Below' 'Within Range'
        'Within Range' 'Below' 'Within Range' 'Above' 'Below']

        """
        # return np.mean(transactions)
        #np.mean[:1], dtype = float 
        #np.where((transactions > 150, "Above") & (transactions >= 130 | transactions <= 150, "Within Range"), & (transactions < 130, "Below"))
    # np.where(transactions[0:1] > 150, "Above", np.where(transactions >= 130 | transactions <= 150, "Within Range", np.where(transactions < 130, "Below")))
    # return transactions[0:,1:] #middle and last column
    #return transactions[:,1] #middle colummn
    # return transactions[::,2] #last columnn
    #return np.mean(transactions[:,1],transactions[::,2])
    #np.where(((transactions[:,1]).astype('float64') / (transactions[::,2]).astype('float64') > 150, "Above") & ((transactions[:,1]).astype('float64') / (transactions[::,2]).astype('float64') >= 130 | (transactions[:,1]).astype('float64') / (transactions[::,2]).astype('float64') <= 150, "Within Range"), & ((transactions[:,1]).astype('float64') / (transactions[::,2]).astype('float64') < 130, "Below"))
    #return (transactions[:,1]).astype('float64') / (transactions[::,2]).astype('float64')
    #return np.where(transactions[:,1].astype('float64') / transactions[:,2].astype('float64') > 150, "Above", np.where(transactions[:,1].astype('float64') / transactions[:,2].astype('float64') >= 130, "Within Range", np.where(transactions[:,1].astype('float64') / transactions[:,2].astype('float64') <= 150, "Within Range", np.where(transactions[:,1].astype('float64') / transactions[:,2].astype('float64') < 130, "Below", "Below"))))
    return np.where(transactions[:,1].astype('float64') / transactions[:,2].astype('float64') > 150, "Above", np.where((transactions[:,1].astype('float64') / transactions[:,2].astype('float64')) >= 130 | (transactions[:,1].astype('float64') /transactions[:,2].astype('float64') <= 150) , "Within Range", "Below"))



def not_stealing(items):
    """
    While you're shopping, you notice that some items you've picked up do not have a price tag.
    Do you steal them? NO! Instead, you decide to be a good person and replace them with another item
    that does have a price.
    - Items with no price will have a value of np.nan.
    - Replace np.nan values with a random price between $5 and $9, inclusive.
    - Return the average of the new prices in the array, rounded to 2 decimal places.
    - DO NOT REMOVE random.seed(1)

    Args:
        items (np.array)
    Returns:
        float

    >> items = np.array([4.63, np.nan, 3.78, 7.12, 12.35, 7.19, np.nan, 1.50, 2.41])

    >> not_stealing(items)
    5.66

    """
    #DO NOT REMOVE#
    random.seed(1)
    ##############
    arr = np.where(np.isnan(items),np.random.randint(5,9),items)
    arra = np.mean(arr)
    return np.round(arra,2)


    # return np.isnan(items)

if __name__ == "__main__":

    pass

    ##Question 1
    store_nums = np.array([15, 12, 8, 3, 4, 3, 6, 5, 7, 4])
    spending_limit = np.array([200, 500, 330, 120, 85, 60, 220, 190, 490, 300])
    print(shopping_spree(spending_limit, store_nums))

    store_nums = np.array([10, 14, 5, 2, 8, 1, 9, 3])
    spending_limit = np.array([220, 400, 330, 130, 280, 50, 250, 170])
    print(shopping_spree(spending_limit, store_nums))

    ##Question 2
    print(serial_numbers(10))
    print(serial_numbers(12))

    ##Question 3
    price_arr1 = np.array([10.25, 12.5, 5.25, 29.5, 2.5], dtype = "float64")
    print(bath_and_body(price_arr1))

    price_arr2 = np.array([3.5, 13.35, 5.5, 13.15, 2.5, 2.5], dtype = "float64")
    print(bath_and_body(price_arr2))

    ##Question 4
    shoe_arr1 = np.array([["Nike", "Adidas", "New Balance"],
                                 ["110.99", "135.99", "94.99"],
                                 ["85.99", "150.99", "105.99"],
                                 ["225.99", "145.99", "130.99"]])
    print(shoe_shopping(shoe_arr1))

    shoe_arr2 = np.array([["Converse", "Vans", "Dr. Martens", "Steve Madden"],
                                 ["82.99", "250.99", "180.99", "109.99"],
                                 ["99.99", "150.99", "115.99", "75.99"],
                                 ["125.99", "115.99", "110.99", "99.99"]])
    print(shoe_shopping(shoe_arr2))

    ##Question 5
    on_sale = np.array([True, False, True, True, True, True, False, False, False, True, False, True, False])
    my_list = np.array(["eggs", "2% milk", "green onions", "whole wheat bread",
                            "onions", "spinach", "peanut butter", "boxed spaghetti",
                            "salt and vinegar chips", "alfredo sauce"])
    prices = np.array([5.13, 4.29, 1.99, 5.19, 8.99, 3.50, 6.79, 2.19, 3.49, 2.09])
    print(coupons(my_list, on_sale, prices))

    ##Question 6
    week1 = np.array([27, 25, 25, 24, 24, 24, 20])
    week2 = np.array([19, 18, 14, 11, 7, 5, 4])
    start_day = 6
    stop_day = 13
    print(missing_bags(week1, week2, start_day, stop_day))

    week3 = np.array([50, 48, 47, 47, 46, 40, 36])
    week4 = np.array([35, 30, 28, 25, 21, 16, 15])
    start_day1 = 6
    stop_day1 = 13
    print(missing_bags(week3, week4, start_day1, stop_day1))

    ##Question 7
    transactions = np.array([['01-31-2022', 5462101, 24752],
    ['02-28-2022', 7081547.30, 34615],
                ['03-31-2022', 3287654.57, 16588],
                ['04-30-2022', 8725851.81, 45621],
                ['05-31-2022', 6730748.72, 26741],
                ['06-30-2022', 9562745.43, 76436],
                ['07-31-2022', 8641735.21, 61448],
                ['08-31-2022', 7641748.57, 52846],
                ['09-30-2022', 7645277.02, 65457],
                ['10-31-2022', 9416274.67, 65109],
                ['11-30-2022', 9841378.97, 57254],
                ['12-31-2022', 10654298.18, 98651]])
    print(purchases(transactions))

    ##Question 8
    items = np.array([4.63, np.nan, 3.78, 7.12, 12.35, 7.19, np.nan, 1.50, 2.41])
    print(not_stealing(items))

    items = np.array([np.nan, np.nan, 6.18, np.nan, 18.42, 2.67, 9.14, np.nan, 14.32])
    print(not_stealing(items))
