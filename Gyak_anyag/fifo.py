#FIFO -> Azt vesszük ki elsőnek amiket beleraktunk

from collections import deque

que = deque([1, 2, 3, 4])
for i in range(2):
    print(que.popleft())

print(que)