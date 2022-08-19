Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple_a=(6,7,"hello",4.5)
>>> print(type(a))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(type(a))
NameError: name 'a' is not defined
>>> print(type(tuple_a))
<class 'tuple'>
>>> print(tuple_a)
(6, 7, 'hello', 4.5)
>>> a=(1,)
>>> print(a)
(1,)
>>> print(tuple[1])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(tuple[1])
TypeError: 'type' object is not subscriptable
>>> print(tuple_a[1])
7
>>> tuple_a[1]=8
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple_a[1]=8
TypeError: 'tuple' object does not support item assignment
>>> a="red"
>>> tuple_a=tuple(a)
>>> print(tuple_a)
('r', 'e', 'd')
>>> tuple_a=list(a)
>>> print(tuple_a)
['r', 'e', 'd']
>>> tuple_a=tuple(tuple_a)
>>> print(tuple_a)
('r', 'e', 'd')
>>> tuple_b=tuple(range(5))
>>> print(tuple_b)
(0, 1, 2, 3, 4)
>>> print(tuple_b in 5)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(tuple_b in 5)
TypeError: argument of type 'int' is not iterable
>>> print (5 in tuple_b)
False
>>> print(3 in tuple_b)
True
>>> print(tuple_a)
('r', 'e', 'd')
>>> (s1,s2,s3)=tuple_a
>>> print(s1)
r
>>> print(s2)
e
>>> print(s3)
d
>>> 
