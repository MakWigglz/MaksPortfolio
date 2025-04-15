import random
import string

def generate_random_string(length=2):
    """Generates a random string of the specified length using lowercase letters."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Create a list of 50 two-character strings
string_list = [generate_random_string() for _ in range(50)]

# Convert the list to a tuple
string_tuple = tuple(string_list)

print(string_tuple)
print(f"Number of elements in the tuple: {len(string_tuple)}")
print(f"Length of each string: {len(string_tuple[0]) if string_tuple else 0}")
