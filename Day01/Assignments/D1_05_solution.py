"""
 - For a given sentence, write a function that reverses the word order.
"""
def reverse_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))


print(reverse_words("Python is a fantastic language."))
