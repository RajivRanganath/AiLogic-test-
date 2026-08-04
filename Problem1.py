n = int(input())
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))

intervals.sort()

merged = []
for start, end in intervals:
    if merged and start <= merged[-1][1]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

for start, end in merged:
    print(start, end)