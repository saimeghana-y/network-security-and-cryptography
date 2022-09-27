def encrypt(text,s):
  result = ""
  for i in text:
    if (i.isupper()):
        result += chr((ord(i) + s-65) % 26 + 65)
    else:
        result += chr((ord(i) + s - 97) % 26 + 97)
  return result

text = input("Enter plain text: ")
s = int(input("Enter shift value: "))
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher text: " + encrypt(text,s))
