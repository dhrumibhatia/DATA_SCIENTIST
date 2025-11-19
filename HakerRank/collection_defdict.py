from collections import defaultdict

'''
defaultdict(default_factory, [optional_initial_data])

The default_factory is the most important argument. 
It must be a callable (a function, class, or type) that takes no arguments and returns a value.
like list, int, str, or any function etc.

optional_initial_data
is an optional argument that can be used to initialize the defaultdict with 
key-value pairs from another mapping or iterable of key-value pairs.

'''
#counting items using defaultdict
a = ['a', 'b', 'c', 'a', 'b', 'a']
d = defaultdict(int)
print(d)

for i in a:
    d[i] += 1
print(d)  #defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 1})

#grouping items using defaultdict
item = [('fruit','apple'),('vegetable','carrot'),('fruit','banana'),('vegetable','spinach')]
print(item)
grouped = defaultdict(list)

for key, value in item:
    grouped[key].append(value)
print(grouped)  #defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot', 'spinach']})


# Example: Building a simple graph using defaultdict
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
print(f"Graph adjacency list: {dict(graph)}")
