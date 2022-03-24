import os
from datetime import datetime
from ex5_1 import get_random_date, print_function_directory
from ex5_2 import join, get_price

if __name__ == '__main__':

    # Function of the date 5.1
    print("Function of 5.1 , result of getting a random date:")
    get_random_date()
    print("\n")

    # functions of the deep 5.1
    print("Function of 5.1 , result of This is the way-directory")
    print_function_directory()
    print("\n")

    # FUNCTION OF Cup_of_join  5.2
    print("Function of 5.2 , result of Cup_of_join function")
    print(join([3, 4], [2], [9, 8, 3, 1], '@'))
    print("\n")

    # piece_of_cake function printing 5.2
    print("Function of 5.2 , result of piece_of_cake function")
    print(get_price({'chocolate': 20, 'milk': 5}, chocolate=250, milk=120))

