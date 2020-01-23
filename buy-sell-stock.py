def find_max_profit(lst):
	"""Given a list of stock prices by day
	calculate max profit possible"""

	lowest_inx = 0

	for i in range(len(lst)):
		if lst[i] < lst[lowest_inx]:
			lowest_inx = i

	highest = lst[lowest_inx]

	for price in lst[lowest_inx:]:
		if price > highest:
			highest = price

	if highest - lst[lowest_inx] < 0:
		return 0

	return highest - lst[lowest_inx]

print(find_max_profit([7,1,5,3,6,4]))
print(find_max_profit([7,6,4,3,1]))