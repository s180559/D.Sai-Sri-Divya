Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict_a={name:"divya",id:s180559}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dict_a={name:"divya",id:s180559}
NameError: name 'name' is not defined
>>> dict_a={"name":"divya","id":180559}
>>> print(dict_a)
{'name': 'divya', 'id': 180559}
>>> print(type(dict_a))
<class 'dict'>
>>> print(len(dict_a))
2
>>> print(dict_a[name])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(dict_a[name])
NameError: name 'name' is not defined
>>> print(dict_a["name"])
divya
>>> print(dict_a.get('name'))
divya
>>> print(dict_a["city"])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(dict_a["city"])
KeyError: 'city'
>>> result='name'in dict_a
>>> print(result)
True
>>> dict_a['mobile_no']=9573396489
>>> print(dict_a)
{'name': 'divya', 'id': 180559, 'mobile_no': 9573396489}
>>> dict_a['mobile_no']=8341883853
>>> print(dict_a)
{'name': 'divya', 'id': 180559, 'mobile_no': 8341883853}
>>> print(dict_a.keys())
dict_keys(['name', 'id', 'mobile_no'])
>>> print(dict_a.values())
dict_values(['divya', 180559, 8341883853])
>>> print(dict_a.items())
dict_items([('name', 'divya'), ('id', 180559), ('mobile_no', 8341883853)])
>>> b=list(dict_a)
>>> print(b)
['name', 'id', 'mobile_no']
>>> dict_b=dict(dict_a)
>>> print(dict_b)
{'name': 'divya', 'id': 180559, 'mobile_no': 8341883853}
>>> print(len(dict_a))
3
>>> dict_b=dict
>>> dict_b=dict_a.copy()
>>> print(dict_b)
{'name': 'divya', 'id': 180559, 'mobile_no': 8341883853}
>>> print(dict_a.pop())
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(dict_a.pop())
TypeError: pop expected at least 1 arguments, got 0
>>> print(dict_a.popitem())
('mobile_no', 8341883853)
>>> print(dict_a.pop("name"))
divya
>>> print(dict_a)
{'id': 180559}
>>> dict_a.clear()
>>> print(dict_a)
{}
>>> 
