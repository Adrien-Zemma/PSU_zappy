
def map(valMax, val):
	while val < 0:
		val += valMax
	while val >= valMax:
		val -= valMax
	return val
