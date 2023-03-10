def fibonacci(n):
    a = 1
    b = 1
    fib_list = [a,b]
    if n <= 1:
        return n
    else:
        for i in range(2,n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])     
        return fib_list
user_val = int(input('Enter the number :: '))

print(fibonacci(user_val))