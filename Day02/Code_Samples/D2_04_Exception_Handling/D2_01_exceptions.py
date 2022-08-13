"""
 - These attempts will generate different errors.
 - Note: uncomment to try.
"""
# x = int("random string")  # ValueError
# x = "1" + 2  # TypeError
# print(y)  # NameError
# x = 1 / 0  # ZeroDivisionError
# x = pow(2.0, 1_000_000)  # OverflowError







"""
 - Construct for handling exceptions uses 'try/except' combination.
 - Note: uncomment to try.
"""
# try:
#     x = int(input("Enter an integer:"))
# except ValueError:
#     print("The value that was entered is not integer!")








"""
 - You can catch different errors in except block.
 - Note: uncomment to try.
"""
# try:
#     x = int(input("Enter an integer:"))
#     y = int(input("Enter another integer:"))
#     print(x / y)
# except TypeError:
#     print("The value that was entered is not integer!")
# except ZeroDivisionError:
#     print("The second number must not be 0!")








"""
 - The full construct has 'else' and 'finally' blocks too.
"""
try:
    x = int(input("Enter an integer:"))
    y = int(input("Enter another integer:"))
    print(x / y)
except TypeError:
    print("The value that was entered is not integer!")
except ZeroDivisionError:
    print("The second number must not be 0!")
except Exception as err:
    print(err)
else:
    print("This runs after try did not throw exceptions!")
finally:
    print("This always runs!")








"""
 - Manually throwing exception can be done using 'raise'
 - Note: uncomment to try.
"""
# from datetime import datetime
# current_date = datetime.now()
# print("Current date is: " + current_date.strftime('%Y-%m-%d'))

# date_input = input("Enter date in yyyy-mm-dd format: ")
# date_formatted = datetime.strptime(date_input, '%Y-%m-%d')
# print("Date you entered is: " + date_formatted.strftime('%Y-%m-%d'))

# if (date_formatted.date() < current_date.date()):
#     raise Exception("Date you entered cannot be in the past")






"""
 - Another way to raise exception is using assertions.
 - The proper use of assertions is to inform developers about unrecoverable errors in a program.
 - Assertions are not intended to signal expected error conditions, like a Zero Division error,
    where a user can take corrective actions or just try again.
 - Assertions are meant to be internal self-checks for your program.
    They work by declaring some conditions as impossible in your code.
    If one of these conditions does not hold, that means there is a bug in the program.
 - Note: uncomment to try.
"""
# from datetime import datetime
# current_date = datetime.now()
# print("Current date is: " + current_date.strftime('%Y-%m-%d'))

# date_input = input("Enter date in yyyy-mm-dd format: ")
# date_formatted = datetime.strptime(date_input, '%Y-%m-%d')
# print("Date you entered is: " + date_formatted.strftime('%Y-%m-%d'))

# assert(date_formatted.date() >= current_date.date()
#        ), "Date you entered cannot be in the past"
