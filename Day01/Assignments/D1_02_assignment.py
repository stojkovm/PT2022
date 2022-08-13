"""
 - Create command line interface(CLI) using match-case construct.
 - When user types:
  - 'show' - print "List of all files using command show"
  - 'mkdir folder1' - print "Creating new directory folder1 using command mkdir"
  - 'delete --ask text1.txt text2.txt' - print "Removing files: text1.txt text2.txt"
  - 'remove --ask text1.txt text2.txt' - print "Removing files: text1.txt text2.txt"
  - <nothing_above> - print "Command not found!"
"""

command = input("Please type a command: ")
