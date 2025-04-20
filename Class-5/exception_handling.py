
# 🔥 Exception Handling in Simple Words
# Block  	 Purpose
# try	 =>  Risky code ko check karne ke liye
# except =>  Error aane par handle karne ke liye
# else   =>  Jab koi error na aaye tab chalega
# finally=>  Hamesha chalega (Error ho ya na ho)

# Example 1:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")

# Example 2:
def eat_ZingerBurger(is_fasting:bool):
    if is_fasting:
        raise Exception("You are fasting, you cannot eat Zinger Burger")
    else:
        print("Eating Zinger Burger")
    
try:
        eat_ZingerBurger(True)
except Exception as e:
        print("Exception occurred:", e)


# Example 3:
# Find Percentage And Grade Calcuator
try:
    obtainedMarks = float(input("Enter Your Exam Obtained Marks? "))
    totalMarks =  float(input("Enter Your Exam Total Marks? "))

    percentage  = obtainedMarks * 100 /  totalMarks
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Your Percentage is : {percentage}")
    if percentage >= 70:
        print("Congratulation! You Got A+ Grade")
    elif percentage >= 60 and percentage < 70:
        print("Congratulation! You Got B Grade")
    elif percentage >= 50 and percentage < 60:
        print("Good! You Got C Grade")
    elif percentage >= 30 and percentage < 50:
        print("Not Bad! You Got D Grade")
    else:
        print("Sorry! You have failed, but don't worry. Try again, and I hope you will achieve better marks next time.")
finally:
    print("Thank you for using the Percentage and Grade Calculator!")






        