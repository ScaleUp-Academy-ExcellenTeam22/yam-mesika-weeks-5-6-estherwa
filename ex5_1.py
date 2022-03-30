import os
from random import randrange
from datetime import timedelta, datetime


def print_function_directory():
    """
    This function will go to the directory given by the user and check if its a directory and in case is a
    directory it will print those that start with deep
    @return: does not return anything.
    :param: directory_path : gets the path by the user
    """
    directory_path = input("Enter the path to directory:")
    print("is directory" if os.path.isdir(directory_path) else "not a directory")
    print([directory for directory in os.listdir(directory_path) if directory.startswith("deep")])


# ----------------------------------------------------------------------------------------------------------------------
def get_random_date():
    """
    This is the main function will print a random date between the years of 2008 and 2022 and will check if is monday
    in case It's monday will print the specific message
    :param : starting_date: the starting point of the dates to create a random one in range
    :param : ending_date: the ending point of the dates to create a random one in range

    """
    starting_date = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    ending_date = datetime.strptime('1/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')
    date = create_random_date(starting_date, ending_date)
    print(date)
    check_if_monday(date)


# -----------------------------------------------------------------------------------------------------------------------
def create_random_date(start, end):
    """
   This function will return a random datetime between two datetime
   objects.
   @param: start:gets a random date
   @param: start:gets another date
   @return : returns a new date based on both of the dates received
   """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# ----------------------------------------------------------------------------------------------------------------------

def check_if_monday(date):
    """
     This function will check if the date gotten is Monday and in that case it will print a message
     param date: The function gets a parameter of a date.
     @param: message- gets a message in case that the date given is equal to Monday
     """
    if date.isoweekday() == 1:
        print("I do not have vinaigrette")
# ----------------------------------------------------------------------------------------------------------------------
