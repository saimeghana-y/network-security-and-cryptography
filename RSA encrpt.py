p=int(input('Enter Value of p: ')) #p=7
q=int(input('Enter Value of q: ')) #q=11
e=int(input('Enter Value of e: ')) #e=7
m=int(input('Enter Message: ')) #m=37
n=p*q

cp=(m**e)%n
print('Plain Text: ',m)
print('Cipher Text: ',cp)
