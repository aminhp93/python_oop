def insert_val_at(index, list, value):
	if len(list) < index:
		return False
		
	result = []
	i = 0
	while i < len(list):
		if i != index:
			result.append(list[i])
		else:
			result.append(value)
			result.append(list[i])
		i += 1
	return result
	