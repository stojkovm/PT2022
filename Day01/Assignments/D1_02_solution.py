"""
 - Create command line interface(CLI) using match-case construct.
 - When user types:
  - 'show' - print "List of all files using command show"
  - 'mkdir folder1' - print "Creating new directory folder1 using command mkdir"
  - 'delete --ask text1.txt text2.txt' - print "Removing files: text1.txt text2.txt"
  - 'remove --ask text1.txt text2.txt' - print "Removing files: text1.txt text2.txt"
  - <nothing_above> - print "Command not found!"
"""
"""
 - match...case is more powerful than switch...case in other languages.
"""

command = input("Please type a command: ")

match command.split():
    case ["show"]:
        print(f"List of all files using command {command}")
        # code for printing names of all files
    case ["mkdir", dir_name]:
        print(f"Creating new directory {dir_name} using command mkdir")
        # code for creating directory
    case ["delete" | "remove", *files] if "--ask" in files:
        confirmation = input("Are you sure you want to delete files?\n")
        if confirmation.lower() == "yes":
            files.remove("--ask")
            print(f"Removing files: {files}")
            # code for removing selected files
        else:
            print(f"Aborting action...")
    case _:
        print(f"Command not found!")
