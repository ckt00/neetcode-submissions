def add_two_numbers() -> int:
    x = input()
    z = x.split(",")
    i = []
    for j in z:
        i.append(int(j))
    return sum(i)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
