from stack import Stack


def detect_operator(opt, num1, num2):
	if opt == "*":
		return num1 * num2
	elif opt == "/":
		return num1 / num2
	elif opt == "+":
		return num1 + num2
	else:
		return num1 - num2


def post_eval(exp):
	s = Stack()
	temp = exp.split()
	for item in temp:
		if item.isdigit():
			s.push(int(item))
		else:
			num1 = s.pop()
			num2 = s.pop()
			
			result = detect_operator(item, num2, num1)
			s.push(result)
	return s.pop()


print(post_eval('7 8 + 3 2 + /'))
