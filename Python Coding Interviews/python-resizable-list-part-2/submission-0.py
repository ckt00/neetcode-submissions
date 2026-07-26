from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    x = set(arr2)
    y = sorted(list(x))
    z = []
    for i in arr1:
        if i not in y:
            z.append(i)
    return z



# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
