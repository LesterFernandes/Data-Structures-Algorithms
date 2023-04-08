# this is a fibonacci series - 0,1,1,2,3,5,8,13,21

memo = {}
def fib(n):
    if n in memo.keys():
        return memo[n]
    elif n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
        return f

print(fib(7))
