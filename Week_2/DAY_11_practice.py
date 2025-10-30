# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# List comprehension 
squares = [n**2 for n in numbers]
print("Squares:", squares)

# Filter even numbers using list comprehension
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# Dict comprehension
num_dict = {n: n**2 for n in numbers}
print("Dictionary of number:square:", num_dict)

# Set comprehension
unique_squares = {n**2 for n in numbers}
print("Set of unique squares:", unique_squares)

# Using lambda, map, filter
# Square each number
squared_nums = list(map(lambda n: n**2, numbers))
print("Squares using map + lambda:", squared_nums)

# Filter even numbers
even_nums = list(filter(lambda n: n % 2 == 0, numbers))
print("Evens using filter + lambda:", even_nums)

# --- Using zip ---
names = ["Alice", "Bob", "Charlie"]
ages = [22, 25, 30]
combined = list(zip(names, ages))
print("Zipped lists:", combined)
