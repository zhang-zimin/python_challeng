d ={}
with open('leveltwotext.txt') as f:
    for i in f.read():
        d[i] = d.get(i,0) +1

ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse =True)
print(ls)
print(d)