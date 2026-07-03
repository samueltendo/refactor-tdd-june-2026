def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    
    if n % 3 == 0:
        return "Fizz"
    
    if n % 5 == 0 :
        return "Buzz"
    
    return    str(n)
