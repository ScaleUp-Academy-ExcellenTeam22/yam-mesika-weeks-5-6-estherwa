import os
from random import randrange
from datetime import timedelta, datetime


# This is  ex1
# ----------------------------------------------------------------------------------------------------------------------
def print_function_directory():
    """
          This function will go to the directory given by the user and check if its a directory and in case is a
          directory it will print what starts with deep
          """
    directory_path = input("Enter the path to directory:")

    print("is directory" if (os.path.isdir(directory_path)) else "not a directory")

    print([i for i in os.listdir(directory_path) if i.startswith("deep")])


# ----------------------------------------------------------------------------------------------------------------------

def get_random_date():
    """
       This function will print a random date between the years of 2008 and 2022 and will check if is monday
       in case its monday will print the specific message
       """

    d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')

    date = create_random_date(d1, d2)

    print(date)

    check_if_monday(date)


# -----------------------------------------------------------------------------------------------------------------------
def create_random_date(start, end):
    """
   This function will return a random datetime between two datetime
   objects.
   """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

    # ----------------------------------------------------------------------------------------------------------------------
    """
   This function will check if the day genrated randomly is monday and will print the folloowing message in case is
   monday
   """

def check_if_monday(date):
    if date.isoweekday() == 1:
        print("I do not have vinaigrette")

# ----------------------------------------------------------------------------------------------------------------------
