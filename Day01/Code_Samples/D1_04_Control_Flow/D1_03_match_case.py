"""
 - match...case  
 - We define a variable command and use the 'match' keyword to
    match it to the cases defined after each 'case' keyword.
 - 'match' and 'case' are keywords that only work in a match...case statement.
 - The case _ is equivalent to else in an if-elif-else statement.
"""

command = input("Please type a command (show/delete/quit): ")

match command:
    case "show":
        print(f"List of all files using command {command}")
        # code for printing names of all files
    case "delete":
        print(f"Deleting all files using command {command}")
        # code for deleting all files
    case "quit":
        print(f"Quiting the program...")
        # code for quiting
    case _:
        print(f"Command not found!")
