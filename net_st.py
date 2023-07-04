def netlist1(A, B, C, D):
	net_e = A and B
	net_f = 0
	net_g = not net_f
	Z = net_g ^ net_e
	return Z