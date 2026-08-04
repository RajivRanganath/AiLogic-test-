from collections import deque

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

max_deque = deque()  
min_deque = deque()  

left = 0
bestlen = 0
beststart = 0

for right in range(n):
    while max_deque and arr[max_deque[-1]] <= arr[right]:
        max_deque.pop()
    max_deque.append(right)

    while min_deque and arr[min_deque[-1]] >= arr[right]:
        min_deque.pop()
    min_deque.append(right)

    while arr[max_deque[0]] - arr[min_deque[0]] > k:
        left += 1
        if max_deque[0] < left:
            max_deque.popleft()
        if min_deque[0] < left:
            min_deque.popleft()

    window_len = right - left + 1
    if window_len > bestlen:
        bestlen = window_len
        beststart = left

print(bestlen, beststart + 1)