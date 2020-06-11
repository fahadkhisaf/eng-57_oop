# Intro to OOP  

# What is OOP,
Objects are collections of data that share attributes and methods that can be used or manipulate 
and access certain functional requirements at certain times rather than access all the functions at all times.

# Why OOP. 
Stops the program running redundant lines of code that it is not using, and makes hte code more readable by separating the
main run code from the functions that operate in the background, making it easier for users and other developers to navigate the
code.

### Learning outcomes: 
- 

### Class
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
    
### methods 
The actions or how an object behaves. 

So in the above example, .eat_cookie() could be a method inside the class Cookie

### syntax
```python
class Dog():

    def __init__(self, attri1, attri2, optional_attri='default'):
        self.attribute_1 = attri1,
        self.attribute_2 = attri2,
        self.attribute_3 = optional_attri,

    def method_name(self, arg1):
        # complex block
        arg1 += arg1 + 1 
        return  arg1 
```

### Convention
When creating a class make sure the first letter of the class is capitalised.

## OOP 4 Pillars

### Abstration 
Hiding the real implementation of an app from the user and emphaising only how 
to use the application. 

#### Polymorthism
Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class.

#### Encapsulation 
The ability to limit access from the exterior to method and or attributes.
Hence, making them 'private'. 

### Inheritance
The ability of a subclass to inherit all the behaviour and method from parent class. 
One of the core reasons to use OOP, because it means you write less code. In reality this is debatable, has you end-up having to adapt a lot of methods. 
It also depends how good of a coder you are and ability to abstract effectivly. 






