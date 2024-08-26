# A simple script to classify a number

# Example number
number = 10  # You can change this number to test different conditions

# The 'if' statement checks if the condition (number > 0) is True.
# If it is True, the corresponding block of code is executed.
if number > 0:
    print("The number is positive.")  # This line executes only if number > 0.

# The 'elif' statement stands for "else if".
# It is checked only if the previous 'if' condition was False.
# Here, it checks if the number is equal to 0.
elif number == 0:
    print("The number is zero.")  # This line executes only if number == 0.

# The 'else' statement is the fallback condition.
# It is executed only if all previous 'if' and 'elif' conditions were False.
# Here, it means the number must be less than 0.
else:
    print("The number is negative.")  # This line executes only if number < 0.






