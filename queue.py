#Queue is first-in first-out (FIFO)
from collections import deque
banks = deque(["x","y","z"])
print(banks)
banks.popleft()
banks.popleft()
banks.popleft()
print(banks)

if not banks:
    print("No Persons left")