my_list = (1, 3, 6, 'sdsdsd', 'sqweqwe', 3.4)


def lists (*func_list):
	list_types = []
	for i in func_list:
		list_types.append(type(i))
	return list_types

print (lists(1, 3, 6, 'sdsdsd', 'sqweqwe', 3.4))