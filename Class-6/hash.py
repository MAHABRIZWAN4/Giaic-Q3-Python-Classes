# Hashing ek tareeka hai jisse data ko efficiently store aur retrieve kiya ja sakta hai. Yeh ek function hai jo string ya kisi aur data type ko ek unique number mein convert karta hai, jise hash value kehte hain.

# Hashing kaise kaam karti hai:

# 1. Hash function data ko input ke roop mein leta hai aur ek hash value generate karta hai.
# 2. Yeh hash value ek index ke roop mein use hota hai jahan data store hota hai.
# 3. Jab hum data retrieve karna chahte hain, toh hash function usse phir se hash value mein convert karta hai aur us index par data ko dhundta hai.

# Hashing ke fayde:

# 1. Fast lookup: Hashing ki wajah se data ko bahut jaldi dhundha ja sakta hai.
# 2. Efficient storage: Hashing ki wajah se data ko efficiently store kiya ja sakta hai.

# Real-life example:

# Ek library mein books ko store karna hai. Har book ka ek unique title hota hai. Hum hashing ka use karke books ko store kar sakte hain.

# - Book title ko hash function mein daal kar ek unique index generate kiya jata hai.
# - Us index par book ko store kiya jata hai.
# - Jab hum book ko dhundna chahte hain, toh title ko hash function mein daal kar index generate kiya jata hai aur us index par book ko dhundha jata hai.

# Hashing example
name = "University"
print(hash(name))  # Hash value generate karta hai

# Set example
roles = {"Admin", "Faculty", "Student"}
for role in roles:
    print(hash(role))  # Har role ka hash value generate karta hai


# Set mein items add aur remove karna:


roles = {"Admin", "Faculty", "Student"}
roles.add("Guest")  # Item add karna
print(roles)  # Output: {'Admin', 'Faculty', 'Student', 'Guest'}
roles.remove("Faculty")  # Item remove karna
print(roles)  # Output: {'Admin', 'Student', 'Guest'}


# Hashing ka formula:

# Hashing mein ek common formula hai:

# index = hash_value % size

# Jahan hash_value hash function se generate hota hai aur size table ka size hota hai.





