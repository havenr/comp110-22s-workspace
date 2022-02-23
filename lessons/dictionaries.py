"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)
# Access a value by its key -- "lookup"
# had to use single quotes to not confuse double quotes of f string
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by its key
# schools.pop("Duke")

# Test for existence of a key
# is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")

# or
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("no key 'Duke' found in schools")
    
# Update or reassign a key value pair
schools["UNC"] = 20000


print(schools)

# demonstration of dictionary literals
# empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NSCU": 26150}
print(schools)

# what happens when a key does not exist
print(schools["UNCC"])
