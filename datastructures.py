
#1. LISTS (ORDERED, MUTABLE, DUPLICATES ALLOWED)

print([1, 2].append(3)) # [1, 2, 3]
print([1].extend([2, 3])) # [1, 2, 3]
print([1, 3].insert(1, 2)) # [1, 2, 3]
print([1, 2, 1].remove(1)) # [2, 1]
print([1, 2, 3].pop()) # returns 3
print([1, 2, 3].clear()) # []
print(['a', 'b'].index('b')) # 1
print([1, 2, 1, 1].count(1)) # 3
print([3, 1, 2].sort()) # [1, 2, 3]
print([1, 2, 3].reverse()) # [3, 2, 1]

#2. TUPLES (ORDERED, IMMUTABLE, DUPLICATES ALLOWED)

print((1, 2, 1, 3).count(1)) # 2
print(('a', 'b', 'c').index('b')) # 1   

# 3. SETS (UNORDERED, MUTABLE, UNIQUE ELEMENTS ONLY)


print({1, 2}.add(3)) # {1, 2, 3}
print({1, 2}.remove(1)) # {2}   
print({1, 2}.discard(3)) # {1, 2}
print({1, 2}.pop()) # returns element
print({1, 2}.clear()) # set()
print({1, 2} & {2, 3}) # {2}
print({1, 2} | {2, 3}) # {1, 2, 3}
print({1, 2} - {2, 3}) # {1}
print({1, 2} ^ {2, 3}) # {1, 3}
print({1}.issubset({1, 2})) # True
print({1, 2}.issuperset({1})) # True
print({1}.isdisjoint({2})) # True

# 4. DICTIONARIES (KEY-VALUE PAIRS, MUTABLE, UNIQUE KEYS)

print({'a': 1}.get('b', 0)) # 0
print({'a': 1}.keys()) # dict_keys(['a'])
print({'a': 1}.values()) # dict_values([1])
print({'a': 1}.items()) # dict_items([('a', 1)])
print({'a': 1}.update({'b': 2})) # {'a': 1, 'b': 2}
print({'a': 1}.pop('a')) # 1
print({'a': 1}.popitem()) # ('a', 1)
print({'a': 1}.setdefault('k', 5)) # 5
print(dict.fromkeys(['a', 'b'], 0)) # {'a': 0, 'b': 0}
print({'a': 1}.clear()) # {}
print({'a': 1}.update({'b': 2})) # {'a': 1, 'b': 2}
print({'a': 1}.pop('a')) # 1
print({'a': 1}.pop('b', 0)) # 0
print({'a': 1}.popitem()) # ('a', 1)
print({'a': 1}.setdefault('k', 5)) # 5
