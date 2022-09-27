p=int(input('Enter Value of p: ')) #p=7
q=int(input('Enter Value of q: ')) #q=11
e=int(input('Enter Value of e: ')) #e=7
m=int(input('Enter Message: ')) #m=37
d=0
n=p*q
pin=(p-1)*(q-1)
for i in range(2,pin):
    if (e*i)%pin==1:
        d=i
        break

dp=(m**d)%n
print('Cipher Text: ',m)
print('Plain Text: ',dp)
