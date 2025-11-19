from collections import Counter
'''
Counter
It's a specialized dictionary subclass designed for easily counting hashable objects.

methods of Counter:
- elements(): Returns an iterator over elements repeating each as many times as its count.
- most_common([n]): Returns a list of the n most common elements and their counts from the most common to the least. If n is not specified, it returns all elements in the counter.
- update([iterable-or-mapping]): Adds counts from another iterable or mapping.
- subtract([iterable-or-mapping]): Subtracts counts using another iterable or mapping.
'''
#count word frequency..
sen = 'in python collection pakage is new form of dictionary in python.'
li = Counter(sen.split())
print(li)
# the pytohn and python. will be diffrent therfore count also will be diffrent.
#Output: Counter({'in': 2, 'python': 2, 'collection': 1, 'pakage': 1, 'is': 1, 'new': 1, 'form': 1, 'of': 1, 'dictionary': 1, 'python.': 1})

#for removing the all spacial letters and count the frequncy of the words.
import re

pattern = r'[^\w\s]'
clean_sen = re.sub(pattern,'',sen)

li2  = Counter(clean_sen.split())
print(li2) 
#Counter({'in': 2, 'python': 2, 'collection': 1, 'pakage': 1, 'is': 1, 'new': 1, 'form': 1, 'of': 1, 'dictionary': 1})

## Most common elements --> most_common([n])
print(li2.most_common(2))
#[('in', 2), ('python', 2)]
print(type(i for i in li2.most_common(2)))
#<class 'generator'>
print(type(li2.most_common(2)))             
#<class 'list'>

## Elements --> elements()
a = li2.elements()
# <itertools.chain object at 0x0000020BD396BEB0>
print(a)
print(list(a))

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
c = Counter(fruits)
print(c)
#popular fruits from the list are:-
popular = max(c, key=c.get)
print(popular)  #apple


# Counter arithmetic
a = Counter({'apple': 3, 'banana': 2, 'orange': 1})
b = Counter({'apple': 1, 'banana': 2, 'grape': 4})
# Addition of three Counters (union)
d = a + b + c
print(d)  #Counter({'apple': 7, 'banana': 6, 'grape': 4, 'orange': 4})

# Subtraction of two Counters (diffrence)
e = a - (b - c)
print(e)  #Counter({'apple': 2})

# Intersection of two Counters
f = a & b
print(f)  #Counter({'banana': 2, 'apple': 1})