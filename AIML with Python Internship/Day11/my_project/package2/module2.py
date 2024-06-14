# package2/module2.py

# Import the function from package1.module1
from package1.module1 import hello_from_module1

def hello_from_module2():
    return "Hello from module2 in package2!"

def combined_hello():
    # Use the function from module1
    return hello_from_module1() + " And " + hello_from_module2()
