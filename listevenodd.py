# Program to check if numbers in a list are even or odd
a = [10, 23, 16, 3, 2]
count1 = 0
count2 = 0
for i in a:
    if i % 2 == 0:
        count1 += 1
    else:
        count2 += 1
print(f"count of even numbers: {count1}")
print(f"count of odd numbers: {count2}")