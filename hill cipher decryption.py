str1=input('Enter Cipher Text: ')
import sympy
key=[]
print('Enter Key') #2 3 3 6
for i in range(2):
  l1=list(map(int,input().split(' ')))
  key.append(l1)
a=sympy.Matrix(key)
d=a.adjugate()
# det=d[0]*d[3]-d[1]*d[2]
det=a.det()
d1=[]
j=0
it=2
r=0
for i in range(2,26):
    if (i*det)%26==1:
        r=i
        break
while(it>0):
    d2=[]
    for i in d[j:j+2]:
        if i<0:
            d2.append((i+26)*r)
        else:
            d2.append(i*r)
    d1.append(d2)
    it-=1
    j+=2
final=''
jj=0
it=3
while(it>0):
    text=[]
    for i in str1[jj:jj+2]:
        l1=[]
        l1.append(ord(i)%65)
        text.append(l1) 

    result=[]
    for i in range(len(d1)):
        l3=[]
        for j in range(len(text[0])):
            val=0
            for k in range(len(text)):
                val+=(d1[i][k]*text[k][j])
            l3.append(val%26)
        result.append(l3)
    
    for i in result:
        for j in i:
            final+=(chr(j+97))
    jj+=2
    it-=1
print('Decrypted Text: ',final)
