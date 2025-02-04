from stack import Stack


def convert_postfix_to_infix(exp):
	s = Stack()
	for item in exp:
		if item.isalpha():
			s.push(item)
		
		else:
			opt2 = s.pop()
			opt1 = s.pop()
			s.push(str('(' + opt1 + item + opt2 + ')'))
	
	return s.pop()


print(convert_postfix_to_infix('ABC+*'))
