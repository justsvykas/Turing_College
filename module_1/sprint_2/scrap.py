def example_function(a: int, b: int):
    sum = a + b  # variable 'sum' should not shadow the built-in 'sum'
    return sum


result = example_function(5, 10)
print(result)
