from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
q = int(input())
req = [tuple(map(int,input().split())) for i in range(q)]

avil = {}
for q0,q1 in req:
    avil.setdefault(q0,[]).append(q1)

target = []
tracker = Counter()

for n in arr:
    if n in avil:
        index = tracker[n]
        if index < len(avil[n]):
            target.append(avil[n][index])
            tracker[n]+=1
print(sum(target))
'''
input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''

from collections import deque

queries = [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]
arr = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]

# Preprocess: map first element -> queue of second elements (preserves original order)
value_map = {}
for a, b in queries:
    value_map.setdefault(a, deque()).append(b)

target_values = []
filtered_arr = []

# Single pass over arr
for x in arr:
    q = value_map.get(x)
    if q:
        filtered_arr.append(x)
        target_values.append(q.popleft())  # consume first unused second value

print(f"Filtered Array: {filtered_arr}")
print(f"Target Second Values (q[1]): {target_values}")
print(f"Sum of the target values: {sum(target_values)}")