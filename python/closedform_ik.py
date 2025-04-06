import sympy as sp

"""
Function to return homogeneous transform with no translation and rotation about x by theta, as symbolic math
"""
def Hx(theta):
	ct = sp.cos(theta)
	st = sp.sin(theta)

	Hxc = sp.Matrix( [
		[1, 0, 0, 0],
		[0, ct, -st, 0],
		[0, st, ct, 0],
		[0, 0, 0, 1]
	])
    return Hxc

"""
Function to return homogeneous transform with no translation and rotation about y by theta, as symbolic math
"""
def Hy(theta):
	ct = sp.cos(theta)
	st = sp.sin(theta)

	Hyc = sp.Matrix( [
		[ct, 	0, 	st, 0],
		[0, 	1, 	0, 	0],
		[-st,	0,	ct,	0],
		[0,		0,	0,	1]
	])
    return Hyc

"""
Function to return homogeneous transform with no translation and rotation about z by theta, as symbolic math
"""
def Hz(theta):
	ct = sp.cos(theta)
	st = sp.sin(theta)

	Hzc = sp.Matrix( [
		[ct, 	-st, 	0, 	0],
		[st, 	ct, 	0, 	0],
		[0,		0,		1,	0],
		[0,		0,		0,	1]
	])
    return Hzc

B, Theta1, Theta2, Theta3, vx, vy, vz = sp.symbols('"B" "Theta1" "Theta2" "Theta3" "vx" "vy" "vz"',real=True)

