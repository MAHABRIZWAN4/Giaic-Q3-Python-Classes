# function 

def catch():
    print("Catch the ball ⚽")
catch()

# Now, we will import this module in another file.

def game(item):
    print(f"let's Play with the {item} 🏏")
game("bat")




# function with return keyword 
def catch(item):
    return f"Catch the {item} "

save = print(catch("ball ⚽"))
save1 = print(catch("Chair 🪑"))   







# position  Argument and keyword Argument in function
# 1️⃣ Positional Argument → Order matter karta hai.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("Ali", 25)  # Correct ✅
# greet(25, "Ali")  # Wrong ❌ (Order change ho gaya)


# 1️⃣ Positional Arguments Restriction (* Use Karna)

# Matlab: Sirf positional arguments allow honge, keyword 
# arguments use nahi kar sakte.

def greet(*names, age):  
    print(f"Hello {names}, you are {age} years old!")  

greet("Ali", "Ahmed", 25)  # ✅ Correct (Positional Argument)  
# greet(names="Ali", age=25)  # ❌ Wrong (Keyword Argument allowed nahi)  





# 2️⃣ Keyword Argument → Order matter nahi karta, bas variable 
# name dena zaroori hai.

greet(age=25, name="Ali")  # Correct ✅ (Order change kar sakte hain)



# 2️⃣ Keyword Arguments Restriction (/ Use Karna)
# Matlab: Sirf keyword arguments allow honge, positional arguments
#  use nahi kar sakte.

def greet(name, age, /):  
    print(f"Hello {name}, you are {age} years old!")  

greet(name="Ali", age=25)  # ✅ Correct (Keyword Argument)  
# greet("Ali", 25)  # ❌ Wrong (Positional Argument allowed nahi)  




# 👉 Positional = Pehle likhne ka order follow hota hai

# 👉 Keyword = Naam likh kar order change kar sakte hain


# 🔥 Summary (Short & Easy Table)
# Condition => 	Syntax =>	Example
# Sirf Positional Allowed =>	def fun(*args, param): => ✅ fun("A", "B") ❌ fun(param="B")
# Sirf Keyword Allowed =>	def fun(param, /): => ✅ fun(param="B") ❌ fun("A")



# Default Argument

# A default argument woh hota hai jo apni ek fixed value rakhta hai. 
# Agar function call karte waqt koi value na di jaye, toh default value
#  automatically use hoti hai.

def greet(name="Guest"):  
    print(f"Hello, {name}!")  

greet("Ali")   # ✅ Output: Hello, Ali!  
greet()        # ✅ Output: Hello, Guest! (Default value used)  


