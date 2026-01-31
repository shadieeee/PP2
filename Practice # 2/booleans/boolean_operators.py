is_logged_in = True
is_admin = False

# AND: both must be True
print(is_logged_in and is_admin)  # False

# OR: at least one must be True
print(is_logged_in or is_admin)   # True

# NOT: reverses the boolean
print(not is_logged_in)           # False

# Real-life style example
age = 20
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)
