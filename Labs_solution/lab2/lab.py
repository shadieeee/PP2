# 1 example

import sys
from collections import Counter
year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("YES")
else:
    print("NO")

# 2 example

n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)

# 3 example

a = int(input())
sum = 0

for i in range(1, a+1):
    sum += i

print(sum)

# 4 example

n = int(input())
nums = list(map(int, input().split()))

sum = 0

for i in nums:
    if i > 0:
        sum += 1
print(sum)


# 5 example
a = int(input())
isTrue = True

while a != 1:
    if a % 2 == 0:
        a //= 2  # делим на 2
    else:
        isTrue = False
        break

print("YES" if isTrue else "NO")

# 6 example

n = int(input())
nums = list(map(int, input().split()))

max = -100000000000000000000000

for i in nums:
    if i > max:
        max = i
print(max)

# 7 example

n = int(input())
nums = list(map(int, input().split()))

max = -100000000000000000000000
index = 0

for i in nums:
    if i > max:
        max = i

for i, x in enumerate(nums):
    if x == max:
        i += 1
        index += i
        break
print(index)

# 8 example

n = int(input())
i = 0

while i <= n:
    print(i, end=" ")
    i *= 2

# 9 example

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)

for i in range(n):
    if arr[i] == max_val:
        arr[i] = min_val

print(*arr)

# 10 example

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
print(*arr)

# 11 example

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

l -= 1
r -= 1

arr[l:r+1] = arr[l:r+1][::-1]

print(*arr)

# 12 example

n = int(input())
nums = list(map(int, input().split()))

for i in nums:
    print(i**2, end=" ")

# 13 example

n = int(input())
if n <= 1:
    print("No")
else:
    isTrue = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            isTrue = False
            break
    print("Yes" if isTrue else "No")

# 14 example


n = int(input())
arr = list(map(int, input().split()))

count = {}
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

max_freq = 0
for freq in count.values():
    if freq > max_freq:
        max_freq = freq

most_frequent = float('inf')
for num, freq in count.items():
    if freq == max_freq and num < most_frequent:
        most_frequent = num

print(most_frequent)


# 15 example

n = int(input())
surnames = set()

for _ in range(n):
    surname = input().strip()
    surnames.add(surname)

print(len(surnames))

# 16 example

n = int(input())
arr = list(map(int, input().split()))

seen = []

for num in arr:
    if num in seen:
        print("NO")
    else:
        print("YES")
        seen.append(num)


# 17 example

n = int(input())
numbers = []

for _ in range(n):
    number = input().strip()
    numbers.append(number)

count = 0
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        if numbers.count(num) == 3:
            count += 1

print(count)


# 18 example

n = int(input())
arr = [input().strip() for _ in range(n)]

first_occurrence = {}

for i in range(n):
    if arr[i] not in first_occurrence:
        first_occurrence[arr[i]] = i + 1

for word in sorted(first_occurrence.keys()):
    print(word, first_occurrence[word])


# 19 example

n = int(input())
episodes = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    count = int(line[1])
    if name in episodes:
        episodes[name] += count
    else:
        episodes[name] = count

for name in sorted(episodes.keys()):
    print(name, episodes[name])


# 20 example

input = sys.stdin.readline

n = int(input())
document = {}

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        document[cmd[1]] = cmd[2]
    elif cmd[0] == "get":
        print(document[cmd[1]] if cmd[1]
              in document else f"KE: no key {cmd[1]} found in the document")
