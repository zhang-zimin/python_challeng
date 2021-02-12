import urllib.request

id = 12345
while True:
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={id}"
    res = urllib.request.urlopen(url)
    text = (res.read().decode('utf-8')).split()
    id = eval(text[-1])
    print(id)

 

 