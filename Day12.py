#dequeue
from collections import deque

dq = deque([10, 20, 30])

dq.append(40)       # add right
dq.appendleft(5)    # add left

print("Deque:", dq)

dq.pop()            # remove right
dq.popleft()        # remove left

print("After Operations:", dq)
