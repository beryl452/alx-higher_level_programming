#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	n_el = 0
	while n_el < x:
		try:
			print("{}".format(my_list[n_el]),end="")
		except IndexError:
			break
		n_el += 1
	print("")
	return n_el

