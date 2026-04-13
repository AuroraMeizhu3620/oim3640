print(2**38)


def decrypt(encrypt):
    s = []
    for letter in encrypt:
        if letter.isalpha():
            number = ord(letter)+2
            if number>122:
                number = number-26
                new_letter = chr(number)
                s.append(new_letter)
            else:
                new_letter = chr(number)
                s.append(new_letter)
        else:
            s.append(letter)
    print(''.join(s))

decrypt("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
decrypt('map')
