# import classes here and initialize objects and run methods.
# This seperation will maintain your code more organized following a seperation of concerns.

from cat_object_constructor import *

# initialize a Cat object
garfield_cat_instance = Cat()

# call the method .meow() on object
print(garfield_cat_instance.eat(' tuna'))
print(garfield_cat_instance.make_lasagne())
print(garfield_cat_instance.sleep())
print(garfield_cat_instance.meow(" creepy stranger"))