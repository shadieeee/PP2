# list 1..20
nums = list(range(1, 21))

# filter evens
evens = list(filter(lambda x: x % 2 == 0, nums))

# filter > 10
gt_10 = list(filter(lambda x: x > 10, nums))
# filter %5
fivs = list(filter(lambda x: x%5==0, nums))
# filter 7<x<19
smth = list(filter(lambda x: x>7 and x<19, nums))
print(evens)
print(gt_10)
print(fivs)
print(smth)