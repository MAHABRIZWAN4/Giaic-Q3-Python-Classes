# 🔸 List Comprehension Kya Hoti Hai?
# List comprehension Python ka ek shortcut hota hai jisse hum ek naye list ko existing list se short aur clean code likh kar bana sakte hain.


# 🔹 Basic Syntax:

# [expression for item in list]
# Yani har item ke upar expression apply karke naya list banate hain.

# Real Life Example 1: School Students' Marks
# Agar 5 students ke marks hain aur unke double marks nikalne hain:

# Without list comprehension:

# marks = [10, 20, 30, 40]
# double_marks = []
# for m in marks:
#     double_marks.append(m * 2)
# print(double_marks)



# With list comprehension (easy shortcut):

marks = [10, 20, 30, 40]
print([m * 2 for m in marks]) # Output: [20, 40, 60, 80]


# Real Life Example 2: Students' Names to Uppercase

names = ["ali", "ayesha", "fatima"]
print([name.upper() for name in names]) #Output: ['ALI', 'AYESHA', 'FATIMA']


# Ek Line Me Kaam Ho Jaye (Best Use)

squares = [x*x for x in range(1, 6)]
print(squares)

# fruits = ["apple", "banana", "mango"]
# print([f.capitalize() for f in fruits]) # Output: ['Apple', 'Banana', 'Mango']



