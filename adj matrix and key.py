import sympy
key=[]
print('Enter Key') #2 3 3 6
for i in range(2):
  l1=list(map(int,input().split(' ')))
  key.append(l1)
a=sympy.Matrix(key)
det=a.det()
print("Original matrix is: ",a)
d=a.adjugate()

for i in range(len(d)):
  if d[i]<0:
    d[i] = d[i]+26

final=''
for i in d:
      word=i%26
      final+=(chr(word+65))
print("Adjoint of a matrix is: ",d)
print('Det of the Matrix: ',det)
print('Key for Hill Cipher: ',final)
