#task1
def is_valid_number(number: str) -> bool:
    for digit in number:
        if int(digit) % 2 != 0:
            return False
    return True
n = input().strip()

if is_valid_number(n):
    print("Valid")
else:
    print("Not valid")

#task2

def isusual (num: int) -> bool:
    if num<=0:
        return False
    for i in (2,3,5):
        while num%i==0:
            num//=i
    return num==1
n=int(input())
print( "Yes" if isusual(n) else "No")
 
#task3
def calculate(expr: str) -> str:
    words = {
        "ZER":"0","ONE":"1","TWO":"2","THR":"3",
        "FOU":"4","FIV":"5","SIX":"6","SEV":"7",
        "EIG":"8","NIN":"9"
    }
    rev = {v:k for k,v in words.items()}

    for op in "+-*":
        if op in expr:
            l, r = expr.split(op)
            break

    a = int("".join(words[l[i:i+3]] for i in range(0,len(l),3)))
    b = int("".join(words[r[i:i+3]] for i in range(0,len(r),3)))

    res = a+b if op=="+" else a-b if op=="-" else a*b
    return "".join(rev[d] for d in str(res))


print(calculate(input().strip()))
#task4 
def ew(s: str):
    return s.upper()
so = input()
print(ew(so))


