n,m = map(int,input().split())

a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

print(a, b)
'''
5 2     
a       
a
b
a
b
a      
b

group A size n = 5, group B size m = 2
group A contains 'a', 'a', 'b', 'a', 'b'
group B contains 'a', 'b'
'''
# a = ['a', 'a', 'b', 'a', 'b'] 
# b = ['a', 'b']
#o/t
# 1 2 4
# 3 5

# Without Using DefaultDict
# li = [ [] for i in range(len(b))]

# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i] == a[j]:
#             li[i].append(j+1)
# print(li)
# for i in li:
#     if len(i) == 0:
#         print(-1)
#     else:
#         print(*i)

# Using DefaultDict      
from collections import defaultdict
d = defaultdict(list)

for i in range(1,n+1):
    word = input()
    d[word].append(str(i))

for j in range(m):
    query = input()
    if query in d:
        print(" ".join(d[query]))
    else:
        print(-1)
print(d)