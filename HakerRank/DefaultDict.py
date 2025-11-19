n,m = map(int,input().split())

a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

print(a, b)
# a = ['a', 'a', 'b', 'a', 'b'] 
# b = ['a', 'b']
#o/t
# 1 2 4
# 3 5
li = [ [] for i in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            li[i].append(j+1)
print(li)
for i in li:
    if len(i) == 0:
        print(-1)
    else:
        print(*i)

# Using DefaultDict      
from collections import defaultdict
d = defaultdict(list)
