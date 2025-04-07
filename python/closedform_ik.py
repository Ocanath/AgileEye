import sympy as sp
from sympy_to_solidworks_str import sympy_to_solidworks



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
Function to return homogeneous transform with no translation and rotation about y by theta, as symbolic math
"""
def Ry(theta):
	ct = sp.cos(theta)
	st = sp.sin(theta)

	Ryc = sp.Matrix( [
		[ct, 	0, 	st],
		[0, 	1, 	0],
		[-st,	0,	ct]
	])
	return Ryc

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




vector_targ_is_normalized = False	#flag for indicating vx,vy,vz are pre-normalized (for clarity in reading the math)
B, Theta1, Theta2, Theta3, vx, vy, vz, Otx, Oty, Otz, EyeDiameter = sp.symbols('"B" "Theta1" "Theta2" "Theta3" ("vx") ("vy") ("vz") "Otx" "Oty" "Otz" "EyeDiameter"',real=True)


L0_1 = Hx(-sp.pi/2)
L0_1[1,3] = -B
L0_1[2,3] = B
# sp.pretty_print(L0_1)

L1_2 = Hy(sp.pi/2)
L1_2[0,3] = -B
L1_2[2,3] = B
# sp.pretty_print(L1_2)

H0_1 = Hz(Theta1)*L0_1
H1_2 = Hz(Theta2)*L1_2
H0_2 = H0_1*H1_2
H0_2 = sp.simplify(H0_2)
# sp.pretty_print(H0_2)

#extremely promising: it appears the 'z' coordinate allows us to 
sth2 = (Otz/B)-1

cth1_p = sp.sqrt(1 - sth2**2)
cth1_p = sp.simplify(cth1_p)

cth1_n = -sp.sqrt(1 - sth2**2)
cth1_n = sp.simplify(cth1_n)

# sp.pretty_print(sth2)
# sp.pretty_print(cth1_n)
# sp.pretty_print(cth1_p)


#compute the target o2
VectTarg = sp.Matrix([vx, vy, vz])
theta1_arm1 = sp.atan2(vx, vz)
Ryth = sp.simplify(Ry(theta1_arm1))
Rw_3_x = Ryth*sp.Matrix([-1,0,0])
print("\"Rw_3_xx\" = " + sympy_to_solidworks(Rw_3_x[0]))
print("\"Rw_3_xy\" = " + sympy_to_solidworks(Rw_3_x[1]))
print("\"Rw_3_xz\" = " + sympy_to_solidworks(Rw_3_x[2]))


VtNorm = VectTarg/(sp.sqrt(VectTarg.dot(VectTarg)))
Rw_3_z = VtNorm
print("\"Rw_3_zx\" = " + sympy_to_solidworks(Rw_3_z[0]))
print("\"Rw_3_zy\" = " + sympy_to_solidworks(Rw_3_z[1]))
print("\"Rw_3_zz\" = " + sympy_to_solidworks(Rw_3_z[2]))


Rw_3_y = Rw_3_z.cross(Rw_3_x)
Rw_3_y=sp.simplify(Rw_3_y)
print("\"Rw_3_yx\" = " + sympy_to_solidworks(Rw_3_y[0]))
print("\"Rw_3_yy\" = " + sympy_to_solidworks(Rw_3_y[1]))
print("\"Rw_3_yz\" = " + sympy_to_solidworks(Rw_3_y[2]))

O2Targ = -Rw_3_y*EyeDiameter/2	#eye hole is on the opposite side
print("\"O2Targx\" = " + sympy_to_solidworks(O2Targ[0]))
print("\"O2Targy\" = " + sympy_to_solidworks(O2Targ[1]))
print("\"O2Targz\" = " + sympy_to_solidworks(O2Targ[2]))

# exp_str = str(O2Targ[0]).replace('**', '^').replace('sqrt','sqr')
# print("\"O2Targx\" = " + exp_str)
# exp_str = str(O2Targ[1]).replace('**', '^').replace('sqrt','sqr')
# print("\"O2Targy\" = " + exp_str)
# exp_str = str(O2Targ[2]).replace('**', '^').replace('sqrt','sqr')
# print("\"O2Targz\" = " + exp_str)

