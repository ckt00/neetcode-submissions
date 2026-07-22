from typing import List

def read_integers() -> List[int]:
    x = input()
    y = x.split(",")
    z = []
    for i in y:
        z.append(int(i))
    return z
        
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
