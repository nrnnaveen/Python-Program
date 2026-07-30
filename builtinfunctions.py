
# 1. MATHEMATICAL & NUMERIC FUNCTIONS

print(abs(-1.058)) # whole + numbers ; 1.058
print(pow(2, 3)) # 2^3 = 8
print(round(3.14159, 2)) # 3.14
print(max(4, 12, 7)) # 12
print(min(4, 12, 7)) # 4
print(sum([1, 2, 3, 4])) # 10
print(divmod(10, 3)) # (3, 1)

#2. TYPE CONVERSION & CREATION

print(int("42")) # 42
print(float("3.14")) # 3.14
print(str(100)) # '100'
print(bool(0)) # False
print(list("abc")) # ['a', 'b', 'c']
print(tuple([1, 2, 3])) # (1, 2, 3)
print(set([1, 2, 2, 3])) # {1, 2, 3}
print(dict(a=1, b=2)) # {'a': 1, 'b': 2}
print(chr(65)) # 'A'
print(ord('A')) # 65

#3. ITERABLES & SEQUENCE OPERATIONS


print(len([10, 20, 30])) # 3
print(list(range(1, 5))) # [1, 2, 3, 4]
print(sorted([3, 1, 2])) # [1, 2, 3]
print(list(reversed([1, 2]))) # [2, 1]
print(list(enumerate(['a']))) # [(0, 'a')]
print(list(zip([1], ['a']))) # [(1, 'a')]
print(any([False, True])) # True
print(all([True, False])) # False
print(list(map(str, [1, 2]))) # ['1', '2']
print(list(filter(bool, [0, 1]))) # [1]

#4. INPUT/OUTPUT & INSPECTION FUNCTIONS

print("Hi") # Hi
print(type(42)) # <class 'int'>
print(isinstance(5, int)) # True
print(id(x)) # 1407...
print(dir([])) # ['append'...]
print(help(len)) # Docs
print(callable(print)) # True
print(callable(42)) # False
print(callable(lambda x: x + 1)) # True
print(callable(str)) # True
print(callable(list)) # True
print(callable(dict)) # True
print(callable(set)) # True
print(callable(tuple)) # True
print(callable(int)) # True
print(callable(float)) # True