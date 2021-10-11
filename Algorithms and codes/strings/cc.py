str = str(input("Enter the text : "))
num = int(input("Enter key : "))
num = num % 26

def cc(str,num):
   new = []
   for q in str:
     tdm = ord(q)+num
     if tdm > 122:
       new.append(chr((tdm%122)+96))
     else:
       new.append(chr(tdm))
   new_string = "".join(new)
   return new_string

def decrypt(str,num):
  new = []
  new1 = []
  for q in str:
    tdm = ord(q) + num
    if tdm > 122:
      new.append(chr((tdm % 122) + 96))
    else:
      new.append(chr(tdm))
  new_string = "".join(new)
  for z in new_string:
    tdm = ord(z)-num
    if tdm < 67:
      new1.append(chr(ord(z)-(26-num)))
    else:
      new1.append(chr(tdm))
  new2 = "".join(new1)
  return  new2

print("Encrypted : ")
print(cc(str,num))
print("Decrypted : ")
print(decrypt(str,num))

