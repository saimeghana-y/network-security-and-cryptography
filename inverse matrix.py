from sympy import *
key=[]
print('Enter Key') #2 3 3 6
for i in range(2):
  l1=list(map(int,input().split(' ')))
  key.append(l1)
a=sympy.Matrix(key)
d=a.adjugate()

det=a.det()

r=0
for i in range(2,26):
    if (i*det)%26==1:
        r=i
        break
for i in range(len(d)):
  if d[i]<0:
    d[i] = (d[i]+26)*r
  else:
    d[i] = d[i]*r

final=''
for i in d:
      word=i%26
      final+=(chr(word+65))
print('Inverse Matrix: ',d)
print('Key for Hill Cipher: ',final)
