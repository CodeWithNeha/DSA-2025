def fib(n: int) -> int:
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

num = input("Enter Number:- ")
print(fib(int(num)))