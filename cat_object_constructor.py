# abstract and create the class dog
class Cat():


    # this is a special method
    # it comes defined either way but we can polymorth it and re-write it
    # this methods stands for intialize class object AKA the constractor in other languages.
    # allows us to set attributes to our dog objects
    # ...like.. the poor thing doesnt even has a name
    # self refers to the instance of the object
    def __init__(self, name = 'Garfeild'):
        # setting attribute name to instances Cat class
        self.name = name
        self.age = 12
        self.paws = 4
        self.fur = 'luxurious orange fur'
        self.breed = 'ginger cat'

    # this is a method that can be used by a Cat instance
    def meow(self, person = ''):
        return 'meow, meow, i see you there' + person

    def meow_print(self):
        print('meow, meow')

    def eat(self, food):
        return 'nom nom nom' + food

    def sleep(self):
        return  'zzzzZZZzzzz ZZZzzzZZZ'

    def make_lasagne(self):
        return 'This lasagne is delicous'

    def potty(self):
        return "UHHHHHHH!!!!! AHHHH!!!!"


# this print should not be here
# in this file you define the class cat and add attributes and method to the class.
# that is it
# print('This is a very nice cat')




