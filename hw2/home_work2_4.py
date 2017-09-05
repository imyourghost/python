# На входе два словаря

my_dict1 = {1:2323,2:23231,3:2323,1:2323,1:2323,5:2323}
my_dict2 = {2:2323,1:23254,5:2323}

def dicts (d1, d2):
	key_count=0
	for i in d1.keys():
		for j in d2.keys():
			if i == j:
				key_count +=1
	return key_count
print ('общее количество ключей в словарях ', dicts(my_dict1, my_dict2))