str1=input('Enter Plain text: ')
jj=0
it=3
#key=[[2,3], [3,6]]
key=[]
print('Enter Key') #2 3 3 6
for i in range(2):
  l1=list(map(int,input().split(' ')))
  key.append(l1)

final=''
while(it>0):
    text=[]
    for i in str1[jj:jj+2]:
        l1=[]
        l1.append(ord(i)%97)
        text.append(l1) 
    result=[]
    jj+=2
    it-=1
    for i in range(len(key)):
        l3=[]
        for j in range(len(text[0])):
            val=0
            for k in range(len(text)):
                val+=(key[i][k]*text[k][j])
            l3.append(val%26)
        result.append(l3)

    for i in result:
        for j in i:
            final+=(chr(j+65))
    
print('Encrypted Text: ',final)
