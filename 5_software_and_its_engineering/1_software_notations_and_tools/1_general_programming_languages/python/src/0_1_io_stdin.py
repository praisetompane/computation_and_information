""" 
generic flow:

print("headline")
value = type_conversion_function(input("prompt: "))
# do stuff
print(value) 
"""

# example
print("Please enter two numbers on separate lines")
num_one = int(input("Please enter number: "))
num_two = int(input("Please enter number: "))
print(f"sum: {num_one + num_two}")