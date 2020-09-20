def cipher(arg):
	IC_vals = {0: 'A, F, G, L, Q, R, W', 251142: 'B, M, X', 1506852: 'C, N, Y', 3767130: 'D, O, Z', 7031976: 'E, P', 753426: 'H, S', 2511420: 'I, T', 5273982: 'J, U', 9041112: 'K, V'}
	num_vals = []
	if arg == "all":
		return IC_vals
	else:
		try:
			sep_nums = arg.split(".")
			for nums in sep_nums:
				value = IC_vals.get(int(nums))
				if value is not None:
					num_vals.append(f"Value for {nums} is {value}")
				else:
					return "F"
					break
			return num_vals
		except:
			return False
