#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	n_el = 0
	for el in my_list:
		print("{}".format(el),end="")
		n_el += 1
	return n_el

