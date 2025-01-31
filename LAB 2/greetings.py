#User Function
def say_hello(name):
    return f"Hello, {name}!"
def say_goodbye(name):
    return f"Goodbye, {name}!"

#Main Fumction
from greetings import say_hello, say_goodbye
print(say_hello("Alice")) # Output: Hello, Alice!
print(say_goodbye("Alice")) # Output: Goodbye, Alice!
