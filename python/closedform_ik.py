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
B, Theta1, Theta2, Theta3, vx, vy, vz, Otx, Oty, Otz, EyeDiameter = sp.symbols('"B" "Theta1" "Theta2" "Theta3" "vx" "vy" "vz" "Otx" "Oty" "Otz" "EyeDiameter"',real=True)


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

# Normalize. Not needed
# if vector_targ_is_normalized == False:
# 	VtNorm = VectTarg/sp.sqrt(VectTarg.dot(VectTarg))
# else:
# 	VtNorm = VectTarg



#compute the target o2
VectTarg = sp.Matrix([vx, vy, vz])
theta1_arm1 = sp.atan2(vx, vz)
RW_ref = sp.simplify(Ry(theta1_arm1))
Rref_W = RW_ref.T
# sp.pretty_print(sp.simplify(Rref_W))
Vref = Rref_W*VectTarg
print("Vref = \n")
sp.pretty_print(Vref)
print('------------\n')
theta_tmpref = sp.atan2(Vref[1], Vref[2]) + sp.pi/2

zr = (EyeDiameter/2)*sp.cos(theta_tmpref)
yr = (EyeDiameter/2)*sp.sin(theta_tmpref)


O2Targ = RW_ref*sp.Matrix([0, yr, zr])
O2Targ = sp.simplify(O2Targ)
# sp.pretty_print(O2Targ)

exp_str = str(O2Targ[0]).replace('**', '^').replace('sqrt','sqr')
print("\"O2Targx\" = " + exp_str)
exp_str = str(O2Targ[1]).replace('**', '^').replace('sqrt','sqr')
print("\"O2Targy\" = " + exp_str)
exp_str = str(O2Targ[2]).replace('**', '^').replace('sqrt','sqr')
print("\"O2Targz\" = " + exp_str)

