
def min_max(nums):
    if len(nums) == 0:
        return None
    return min(nums), max(nums)

def safe_divide(a, b):
    if b == 0:
        return "Error"
    return a / b
def even_nums_only(a, b):
    if b%2!=0 or a%2!=0:
        return "Error"
    return a / b
def positive_check(a):
    if a<0:
        return "negative"
    return "positive number!"

print(min_max([5, 2, 9]))
print(min_max([]))
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(even_nums_only(10,2))
print(even_nums_only(5,3))
print(positive_check(12))
print(positive_check(-12))