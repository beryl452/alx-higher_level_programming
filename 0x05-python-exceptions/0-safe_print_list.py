#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	n_el = 0
	try:
		while n_el < x:
			print("{}".format(my_list[n_el]),end="")
			n_el += 1
	except IndexError:
		break
	return n_el

