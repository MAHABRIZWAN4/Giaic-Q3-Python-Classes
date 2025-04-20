# Loops and Iteration in Python
# Introduction to Loops
# Loops ka use repeated tasks ko automate karne ke liye hota hai, 
# jisse time aur effort bachta hai.
# For Example 
# Attendance System → Har student ka naam check karna (For Loop).
# Washing Machine → Kapray fix times ghoomte hain (For Loop).


# Types of Loops
# Python me 2 types ke loops hote hain:
# 1. for loop  → Jab hame pata ho kitni baar repeat karna hai.
# 2. While Loop → Jab hame nahi pata kitni baar repeat karna hai, 
# bas condition true hone tak repeat hota rahe.


# 1. For Loop   → Jab hame pata ho kitni baar repeat karna hai.
# # => for loop hum list , tuple , set, dictionary, range per laga sakte hein.
# Element ko ek ek ker nikaal ker print kerwana..

iftari_items=["Khajoor","Samosa","Rooh Afza","Pakoray","Fruit Chat","Dahi Bhallay","Chana Chaat"];
for i in iftari_items:
    print("-"*50)
    print(i)


# 2. While Loop → Jab hame nahi pata kitni baar repeat karna hai,
# # => Agar list , tuple , set, dictionary, range nahi he to while loop lage ga..


def sum(*n):
    total = 0
    for num in n:
        total += num
    return total


total = sum(23,2,2,2,3,4)
print(total)








