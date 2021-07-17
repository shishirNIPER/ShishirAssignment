import numpy as np

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
#def line_gen(A,B):
# len =10
# dim = A.shape[0]
# x_AB = np.zeros((dim,len))
# lam_1 = np.linspace(0,1,len)
# for i in range(len):
# temp1 = A + lam_1[i]*(B-A)
# x_AB[:,i]= temp1.T
# return x_AB

#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B

#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#Generate line points

def line_norm_eq(n,c,k):
  len =10
  dim = n.shape[0]
  m = omat@n
  m = m/np.linalg.norm(m)
# x_AB = np.zeros((dim,2*len))
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k[0],k[1],len)
# print(lam_1)
# lam_2 = np.linspace(0,k2,len)
  if c==0:
    for i in range(len):
      temp1 = lam_1[i]*m
      x_AB[:,i]= temp1.T
  else:
    A,B = line_icepts(n,c)
    for i in range(len):
      temp1 = A + lam_1[i]*m
      x_AB[:,i]= temp1.T
# temp2 = B + lam_2[i]*m
# x_AB[:,i+len]= temp2.T
  return x_AB

#def line_dir_pt(m,A, dim):
# len = 10
# dim = A.shape[0]
# x_AB = np.zeros((dim,len))
# lam_1 = np.linspace(0,10,len)
# for i in range(len):
# temp1 = A + lam_1[i]*m
# x_AB[:,i]= temp1.T
# return x_AB


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
# P=np.linalg.inv(N.T)@p
  return P

#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)*2-np.linalg.norm(B)*2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)*2-np.linalg.norm(C)*2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r

def mult_line(A_I,b_z,k,m):
 for i in range(m):
  if i == 0:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
  elif i == 1:
    y = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((x[None], y[None]))
  else:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((z,x[None]))
 return z

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])
# -- coding: utf-8 --
"""Assignment2.ipynb
Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1DP8IWd951P0PLgYxb-NHBOwitaDHh8M6
"""

#Code by C.Ramya Tulasi
#May 18, 2021
#Drawing a quadrilateral GOLD
import numpy as np
import matplotlib.pyplot as plt


#Quadrilateral vertices
A = np.array([1,2])
B = np.array([5,4])
C = np.array([3,8]) 
D = np.array([-1,6]) 

import numpy as np
A = np.array([1, 2])
B = np.array([5, 4])
print("Original vectors A and B:")
print(A)
print(B)
print("Inner product of said vectors:")
print(np.inner(A, B))

B = np.array([5, 4])
C = np.array([3, 8])
print("Original vectors B and C:")
print(B)
print(C)
print("Inner product of said vectors:")
print(np.inner(B, C))

C = np.array([3, 8])
D = np.array([-1, 6])
print("Original vectors C and D:")
print(C)
print(D)
print("Inner product of said vectors:")
print(np.inner(C, D))

D = np.array([-1, 6])
A = np.array([1, 2])
print("Original vectors D and A:")
print(D)
print(A)
print("Inner product of said vectors:")
print(np.inner(D, A))


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 +0.03), A[1] * (1 - 0.1) , 'A',weight ="bold")
plt.plot(B[0], B[1], 'o')
plt.text(5.2,4,'B',weight = "bold")
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.05), C[1] * (1 - 0.1) , 'C', weight = "bold")
plt.plot(D[0], D[1], 'o')
plt.text(-1.5,6,'D', weight = "bold")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show
