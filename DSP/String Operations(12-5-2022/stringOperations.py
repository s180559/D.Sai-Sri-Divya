Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="hello"
>>> b="world"
>>> print(a+b)
helloworld
>>> c=a+b
>>> print(len(c))
10
>>> print(a[3])
l
>>> print(b[3])
l
>>> print(a.capitalize())
Hello
>>> print(a.casefold())
hello
>>> c="hello welcome to the python world"
>>> print(c.center())
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(c.center())
TypeError: center() takes at least 1 argument (0 given)
>>> print(a.center(5,"l"))
hello
>>> print(c.count("l"))
4
>>> print(c.encode())
b'hello welcome to the python world'
>>> print(c.endswith("."))
False
>>> print(c.find("l"))
2
>>> print(c.islower())
True
>>> print(c.isalpha())
False
>>> print(c.isspace())
False
>>> print(c.replace("hello","hi"))
hi welcome to the python world
>>> print(c.swapcase())
HELLO WELCOME TO THE PYTHON WORLD
>>> print(c.upper())
HELLO WELCOME TO THE PYTHON WORLD
>>> print(c.title())
Hello Welcome To The Python World
>>> print(c.find("he"))
0
>>> print(c.find("w"))
6
>>> 
