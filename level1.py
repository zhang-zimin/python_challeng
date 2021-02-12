a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = 'map'
b = 'abcdefghijklmnopqrstuvwxyz'
def convert_letter(c):
    if c.isalpha():
        idx = b.index(c)
        idx = (idx +2) %len(b)
        return b[idx]
    else :
        return c
e =""
for i in a:
    e = e + convert_letter(i)
print(e)