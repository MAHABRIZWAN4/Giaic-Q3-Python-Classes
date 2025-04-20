# Lists in Python


# 1️⃣ Ordered (Fix Order & Access by Index)

fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])  # "Apple" milega (index 0)
print(fruits[2])  # "Mango" milega (index 2)




# 2️⃣ Mutable (Change, Add, Remove Items)

fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"  # Banana ko change kar diya Orange se
fruits.append("Grapes")  # New item add kiya
fruits.remove("Apple")  # Apple hata diya
print(fruits)



# 3️⃣ Indexed (Access Items by Position)
 
colors = ["Red", "Blue", "Green"]
print(colors[1])  # Blue milega




# 4️⃣ Dynamic Size (Add/Remove Easily)

nums = [10, 20, 30]
nums.append(40)  # New item add kiya
nums.pop()  # Last item remove kiya
print(nums)






# 5️⃣ Heterogeneous (Different Data Types Allowed)

# data = [25, "Ali", 3.14, True]
# print(data)




# 6️⃣ Supports Duplicate Values

nums = [1, 2, 2, 3, 4, 4, 5]
print(nums)


# ✅ Dynamic aur Mutable me farq hai!

# 🔹 Mutable:

# List ke existing elements ko change kar sakte hain.
# Example: Value update, delete ya replace karna.
# 🔹 Dynamic:

# List ka size automatically change hota hai (grow/shrink).
# Example: Naye elements add ya remove karna.



