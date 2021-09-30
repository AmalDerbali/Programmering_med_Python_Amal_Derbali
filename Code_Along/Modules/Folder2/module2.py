from sys import path
path.append("Folder1")

import module1

def say_hello2():
    print(f"{__name__} says hello")

module1.say_hello1()