numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Combine filter and map in a single expression
result = list(map(lambda x: x*x, filter(lambda x: x%3==0, numbers)))
print(result)
