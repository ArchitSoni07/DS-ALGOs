def cc(str,num):
    new = []
    num = num % 26
    for q in str:
        tdm = ord(q)+num
        if tdm > 122:
            new.append(chr((tdm%122)+96))
        else:
            new.append(chr(tdm))
    new_string = "".join(new)
    return new_string
print(cc("abc",124))
print(cc("abc",20))



