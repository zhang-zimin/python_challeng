import pickle

def convert_line(line):
    res = ''
    for i in line:
        res = res + i[0]*int(i[1])
    print(res)
with open(r'banner.p','rb') as f:
    data = pickle.load(f)

for line in data:
    convert_line(line)