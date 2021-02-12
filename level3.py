import re
with open('pythonchallenge\levelthree.txt') as f:
    text = f.read()
    res = re.findall('[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]',text)
res = ''.join(res)
print(res)
        