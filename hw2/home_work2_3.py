# На входе список, на выходые словарь с типом данных с количеством вхождений

my_list = [1, 3, 6, 'sdsdsd', 'sqweqwe', 3.4]
my_dict = {}

def lists (func_list):
	int_count=0
	str_count=0
	flt_count=0
	complex_count=0
	for i in func_list:
		if isinstance (i, int):
			int_count +=1
			my_dict.update ({type(i): int_count})
		elif isinstance (i, str):
			str_count +=1
			my_dict.update ({type(i): str_count})
		elif isinstance (i, float):
			flt_count +=1
			my_dict.update ({type(i): flt_count})
		elif isinstance (i, complex):
			cmpl_count +=1
			my_dict.update ({type(i): cmpl_count})
	return my_dict

print (lists(my_list))