_fib_cache={1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89}
def fibonacci(n):
    result = _fib_cache.get(n)
    if result is None:
        result = fibonacci(n - 2) + fibonacci(n - 1)
        _fib_cache[n] = result
    return result

print(fibonacci(1000) )