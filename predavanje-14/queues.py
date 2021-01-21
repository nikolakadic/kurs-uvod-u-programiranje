from collections import deque

tunel = deque([1,2,3,4,5,6,7])

tunel.append(8)

tunel.popleft()

print(tunel)