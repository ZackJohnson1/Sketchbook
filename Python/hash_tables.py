# HASH TABLES EXAMPLE

# Initialize a hash table (dictionary)
hash_table = {}

# Create a profile dictionary and insert it into the hash table using an ID or name as the key
profile = {
    'name': 'John',
    'age': 26,
    'city': 'New York'
}
hash_table["John's Profile"] = profile

# Retrieve values from the profile
print(hash_table["John's Profile"]['name'])  # Output: John
print(hash_table["John's Profile"]['age'])   # Output: 25

# Check if a key exists in the profile
if "city" in hash_table["John's Profile"]:
    print("City is:", hash_table["John's Profile"]['city'])  # Output: City is: New York

# Update value in the profile
hash_table["John's Profile"]['city'] = "San Francisco"
print(hash_table["John's Profile"]['city'])  # Output: San Francisco

# Delete a key-value pair from the profile
del hash_table["John's Profile"]['age']
print(hash_table["John's Profile"])  # Output: {'name': 'John', 'city': 'San Francisco'}

# Loop through the profile in the hash table
for key, value in hash_table["John's Profile"].items():
    print(key, ":", value)
