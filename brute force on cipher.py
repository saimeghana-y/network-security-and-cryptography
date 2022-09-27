cipher_text=input("Enter Cipher Text: ")
for i in range(26):
  hack=''
  for j in range(len(cipher_text)):
      if (cipher_text[j].isupper()):
        hack+=chr((ord(cipher_text[j])-i-65)%26+65)
      else:
        hack+=chr((ord(cipher_text[j])-i-97)%26+97)
  print(hack)
