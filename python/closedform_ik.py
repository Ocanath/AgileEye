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




B, Theta1, Theta2, Theta3, vx, vy, vz, Otx, Oty, Otz = sp.symbols('"BasePlaneDistance" "Theta1" "Theta2" "Theta3" ("vx") ("vy") ("vz") "O2Targx" "O2Targy" "O2Targz" ',real=True)

#compute the target o2
"""
Rationale of this method:

1. VectTarg normalized is always the z axis of the output coordinate frame.
2. The x axis will always intersect with the single link rotational axis pin. That means the x axis will be determined by theta
	of the single link rotational axis/actuator, which is defined as atan2(vx/vy). So it's equal to a unit x vector rotated by Y by that amount.
	In the case of my robot, it's not actually a unit x, but a negative unit x, because of how I constrained everything, but that's fine.
3. The y axis, which is where the o2 pin point will be located, is just normal to both of those vectors.

And there you have it.
"""
print("-----------------------------------------------------------------------------------------")
print("Solidworks Equations for setting up O2 and visual references/confirmation of that process\n\n")
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

O2Targ = -Rw_3_y*B	#eye hole is on the opposite side
print("\"O2Targx\" = " + sympy_to_solidworks(O2Targ[0]))
print("\"O2Targy\" = " + sympy_to_solidworks(O2Targ[1]))
print("\"O2Targz\" = " + sympy_to_solidworks(O2Targ[2]))


print("-----------------------------------------------------------------------------------END\n\n")





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
print("H0_2 for the actuator with two links\r\n-------------------------------------")
sp.pretty_print(H0_2[0:3,3])
print("---------------------------------------\n\n")

eq1 = sp.Eq(H0_2[2,3], Otz)
# sp.pretty_print(eq1)
theta2_sols = sp.solve(eq1, Theta2)
# print("\"theta2_s1\" = " + sympy_to_solidworks(theta2_sols[0]))
# print("\"theta2_s2\" = " + sympy_to_solidworks(theta2_sols[0]))
xth1 = sp.cos(theta2_sols[0])
print("\"xth1\" = " + sympy_to_solidworks(xth1))
yth1 = sp.sin(theta2_sols[0])
print("\"yth1\" = " + sympy_to_solidworks(yth1))
theta2_1 = sp.atan2(yth1, xth1)
print("\"theta2_1\" = " + sympy_to_solidworks(theta2_1))
# sp.pretty_print(theta2_sols)

print("\n\n")

eq2 = sp.Eq(H0_2[1,3],Oty)
theta1_sols_y = sp.solve(eq2, Theta1)
# print("theta1_s1")
# sp.pretty_print(theta1_sols_y)


eq3 = sp.Eq(H0_2[0,3],Otx)
theta1_sols_x = sp.solve(eq3, Theta1)
# print("theta1 = ")
# sp.pretty_print(theta1_sols_x)




#extremely promising: it appears the 'z' coordinate allows us to 
sth2 = (Otz/B)-1

cth1_p = sp.sqrt(1 - sth2**2)
cth1_p = sp.simplify(cth1_p)

cth1_n = -sp.sqrt(1 - sth2**2)
cth1_n = sp.simplify(cth1_n)


