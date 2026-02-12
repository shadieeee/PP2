# list numbers
nums = [1, 2, 3, 4]

# map squares
squares = list(map(lambda x: x * x, nums))

# map plus 10
plus_10 = list(map(lambda x: x + 10, nums))

powerr = list(map(lambda x: x**2, nums))
doubled = list(map(lambda x: x*2, nums))

print(nums)
print(squares)
print(plus_10)
print (powerr)
print (doubled)