import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    x = []
    y = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(max_heap, pair)
    for i in range(len(max_heap)):
        x.append(heapq.heappop(max_heap))
    for j in x:
        y.append(j[1])
        
    return y




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
