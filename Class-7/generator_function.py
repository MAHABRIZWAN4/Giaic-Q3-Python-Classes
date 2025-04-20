# Generator function Python mein ek **special type ka function** hota hai jo data ko **ek hi waqt mein thoda thoda** return karta hai — yani **“pause & resume”** karta hai. Ye `yield` keyword ka use karta hai instead of `return`.

# Socho tum ek juice bana rahe ho, aur har glass mein **aadha aadha** juice dal rahe ho.  
# Ek waqt mein poora jug khali nahi kar rahe — **aadha glass bharo, ruk jao**, phir doosra glass bharo... yehi kaam generator karta hai!

# Normal Function: Poora kaam ek hi baar mein
def normal():
    return [1, 2, 3]
print(normal())  # Output: [1, 2, 3]
# Generator Function: Thoda thoda kaam
def generator():
    yield 1
    yield 2
    yield 3
gen = generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Typing Effect Example
import time
def typing(text):
    for char in text:
        yield char  # har character thoda thoda return karega

chat = typing("Hello Mahab!")
for letter in chat:
    print(letter, end='', flush=True)
    time.sleep(0.1)

###  Generator Function Example:
def greet():
    yield "Hello"
    yield "Mahab"

g = greet()
print(next(g))  # Output: Hello
print(next(g))  # Output: Mahab

### 🔁 Generator ka Faida:
# 1. Memory save karta hai (poora data nahi rakhta)
# 2. Fast hota hai jab data zyada ho
# 3. Pause aur resume hota hai (like YouTube video!)

### 💡 Note:
# - `yield` = pause karke value de deta hai
# - `next()` = generator ko dobara chalu karta hai next value ke liye
# - For loop bhi `next()` jaise hi use karta hai internally


