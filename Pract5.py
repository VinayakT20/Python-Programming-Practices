a = int(input("Enter a number: "))

def fibonacci_of(n):
    if (n==1 or n==0):
        return n
    else:
        m = fibonacci_of(n-1)+fibonacci_of(n-2)
        return m

print(fibonacci_of(a))
