#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	n_el = 0
	for i in range(x):
		try:
			print("{:d}".format(my_list[i]), end="")
		except (ValueError, TypeError):
			continue
		else:
			n_el += 1
	print()
	return n_el

