# 1 example
y = int(input())
if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
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

n = int(input())
a = list(map(int, input().split()))
print(sum(a))

# 4 example
n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i > 0: 
        cnt += 1
print(cnt)


# 5 example
n = int(input())

while n > 1:
    if n % 2 != 0:
        print("NO")
        break
    n = n // 2
else:
    print("YES")

# 6 example

n = int(input())
a = list(map(int, input().split()))
print(max(a))

# 7 example

n = int(input())
a = list(map(int, input().split()))
mx = max(a)
for i in range(len(a)):
    if a[i] == mx:
        print(i + 1)
        break

# 8 example

n = int(input())
i = 0

while i <= n:
    print(i, end=" ")
    i *= 2

# 9 example
n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
mn = min(arr)
for i in range(n):
    if arr[i] == mx:
        arr[i] = mn
for x in arr:
    print(x, end=" ")

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
f = {}
for _ in range(n):
    num = input().strip()
    if num in f:
        f[num] += 1
    else:
        f[num] = 1
cnt = 0
for k in f:
    if f[k] == 3:
        cnt += 1

print(cnt)


# 18 example

n = int(input())
first = {}
for i in range(1, n+1):
    s = input().strip()
    if s not in first:
        first[s] = i

for k in sorted(first):
    print(k, first[k])


# 19 example

n = int(input())
d = {}
for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s in d:
        d[s] += k
    else:
        d[s] = k

for name in sorted(d):
    print(name, d[name])

# 20 example

n = int(input())
doc = {}

for _ in range(n):
    parts = input().split()
    if parts[0] == "set":
        _, key, value = parts
        doc[key] = value
    elif parts[0] == "get":
        _, key = parts
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")

