p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
key=[1, 0, 1, 0, 0, 0, 0, 0, 1, 0]

p10key=[]
for i in range(len(p10)):
  p10key.append(key[p10[i]-1])

l=p10key[:5]
r=p10key[5:]

ls1=[]
ls1=l[1:]+l[0:1]
rs1=[]
rs1=r[1:]+r[0:1]

p10key=ls1+rs1
key1=[]
for i in range(len(p8)):
  key1.append(p10key[p8[i]-1])

ls2=[]
ls2=ls1[2:]+ls1[0:2]
rs2=[]
rs2=rs1[2:]+rs1[0:2]

p10key=ls2+rs2
key2=[]
for i in range(len(p8)):
  key2.append(p10key[p8[i]-1])

print('Key1: ',key1)
print('Key2: ',key2)

