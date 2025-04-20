## 🔹 OOP Kya Hai?
# **OOP ek tareeqa hai code likhne ka** jahan hum apni real life cheezon ko "objects" ki form mein represent karte hain.



## 🔹 2 Sabse Important Cheezein:
# 1. **Class** → Naqsha (blueprint)
# 2. **Object** → Asli cheez (real thing)



## 🧃 Real Life Example:
# Socho ek **"Juice Machine"** hai (yeh hogayi class)  
# Us machine se niklay **"Juice"** glasses banenge (yeh honge objects)



## ✅ Example 
# Class banayi

class  Student():
 def __init__(self):   # Magic function   # self hamre pass jo hum object bana rahe hein us ka instance he ...
        # self = {}
        self.name = "Osama"
        # self = {name = "Osama"}

        self.roll_number = "GIAIC0037354"
        # self = {name = "Osama", roll_number = "GIAIC0037354"}

s1 = Student()
print(s1.name)
print(s1.roll_number)

s2 = Student()
print(s2.name)

# init ka func hamare pass object banaye ga self ki help se 





class  Student():
    def __init__(self, roll:str):   # Magic function   # self hamre pass jo hum object bana rahe hein us ka instance he ...
        # self = {}
        self.name = "Osama"
        # self = {name = "Osama"}

        self.roll_number = roll
        # self = {name = "Osama", roll_number = "GIAIC0037354"}


s1 = Student(roll="423")
print(s1.name)
print(s1.roll_number)

s2 = Student(roll="62534")
print(s2.name)
print(s2.roll_number)



class Juice():
    def __init__(self, flavor):  # jab object banta hai to yeh function chal jaata hai
        self.flavor = flavor

    def drink(self):
        print(f"You are drinking {self.flavor} juice 🍹")

# Object banaye
mango = Juice("Mango")
apple = Juice("Apple")

# Call kiya method
mango.drink()   # Output: You are drinking Mango juice 🍹
apple.drink()   # Output: You are drinking Apple juice 🍹


# ## 🧠 Easy Words:
# | Term         | Matlab                              |
# |--------------|--------------------------------------|
# | Class        | Naqsha / Design                     |
# | Object       | Asli cheez jo class se bani hai     |
# | `__init__()` | Auto function jab object banta hai  |
# | `self`       | Us object ki apni pehchan            |



