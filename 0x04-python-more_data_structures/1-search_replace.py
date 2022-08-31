#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [ element == search ? replace : element for element in my_list]
