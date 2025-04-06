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





B, Theta1, Theta2, Theta3, vx, vy, vz, Otx, Oty, Otz = sp.symbols('"B" "Theta1" "Theta2" "Theta3" "vx" "vy" "vz" "Otx" "Oty" "Otz"',real=True)


L0_1 = Hx(-sp.pi/2)
L0_1[1,3] = -B
L0_1[2,3] = B
sp.pretty_print(L0_1)

L1_2 = Hy(sp.pi/2)
L1_2[0,3] = -B
L1_2[2,3] = B
sp.pretty_print(L1_2)

H0_1 = Hz(Theta1)*L0_1
H1_2 = Hz(Theta2)*L1_2
H0_2 = H0_1*H1_2
H0_2 = sp.simplify(H0_2)
sp.pretty_print(H0_2)

#extremely promising: it appears the 'z' coordinate allows us to 
sth2 = (Otz/B)-1

cth1_p = sp.sqrt(1 - sth2**2)
cth1_p = sp.simplify(cth1_p)

cth1_n = -sp.sqrt(1 - sth2**2)
cth1_n = sp.simplify(cth1_n)

sp.pretty_print(sth2)
sp.pretty_print(cth1_n)
sp.pretty_print(cth1_p)


VectTarg = sp.Matrix([vx, vy, vz])
O2Targ = sp.Matrix([Otx, Oty, Otz])


VtNorm = VectTarg#/sp.sqrt(VectTarg.dot(VectTarg))

j = sp.Matrix([0, 1, 0])
TargVx = j.cross(VtNorm)
TargVy = VtNorm.cross(TargVx)
TargVz = VtNorm
Rw_3 = sp.Matrix([
	[TargVx[0], TargVy[0], TargVz[0]],
	[TargVx[1], TargVy[1], TargVz[1]],
	[TargVx[2], TargVy[2], TargVz[2]]

])
sp.pretty_print(Rw_3)
