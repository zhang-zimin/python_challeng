import os


start = 90052
while True: 
    with open(fr'E:\code\pythonchallenge\level6\{start}.txt','r') as f:
        text = f.read().split()
        start = text[-1]
        print(start)

