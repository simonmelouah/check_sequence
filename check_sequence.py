condition = True
array = []

def get_number(array=True):
	while condition:
		if array:
			value = raw_input("Enter an array size: ")
		else:
			value = raw_input("Enter a number: ")
		try:
			value = int(value)
			return value
		except:
			print "Woops! Not a number..."

def check_if_list_contains_sequence(array):
	sequence = "1, 2, 3"
	string_array = ', '.join(str(i) for i in array)
	print string_array
	if sequence in string_array:
		return True
	else:
		return False

array_size = get_number()
for i in range(0, array_size):
	value = get_number(False)
	array.append(value)

print array
check_result = check_if_list_contains_sequence(array)
print check_result
