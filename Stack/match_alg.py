from stack import Stack


def is_match(pattern):
	pat_1 = '({'
	pat_2 = ')}'
	s = Stack()
	
	for item in pattern:
		
		if item in pat_1:
			s.push(item)
		
		elif item in pat_2:
			if s.is_empty():
				return False
			
			if pat_2.index(item) != pat_1.index(s.pop()):
				return False
	
	return s.is_empty()


print(is_match('({})'))