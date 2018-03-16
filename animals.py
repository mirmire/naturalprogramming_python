#!/usr/bin/python3
#  Animals.py   Copyright (c) 2005 Kari Laitinen

#  http://www.naturalprogramming.com

#  2006-04-21  File created.
#  2006-05-22  Last modification.

#  Solution and conversion to Python version 3 by Prakash Acharya, 16-03-2018
#  Solution also modified to meet PEP8 guidelines for formatting

#  The Animal class in this program contains a constructor, i.e., __init__()
#  method, that accepts two types of actual parameters (arguments).

#  In Python classes there can be only one constructor because
#  Python methods cannot be overloaded in the same way as, for example,
#  Java methods.


class Animal:

    def __init__(self, given_parameter):

        if isinstance(given_parameter, str):

            #  The given parameter is a string. We suppose that a new
            #  Animal object with the given species name is being constructed.

            self.species_name = given_parameter
            self.stomach_contents = ""
        elif isinstance(given_parameter, Animal):

            # A reference to an Animal object was given as an actual parameter.
            # The new Animal object will be a copy of the given Animal object.

            self.species_name = given_parameter.species_name
            self.stomach_contents = given_parameter.stomach_contents

        else:
            print("\n Unacceptable object was given to Animal constructor.")

    def feed(self, food_for_this_animal):

        self.stomach_contents += food_for_this_animal + ","

    def make_speak(self):

        print("\nHello, I am a {0}.\nI have eaten: {1}\n"
              .format(self.species_name, self.stomach_contents))


#  The main program begins here.

cat_object = Animal("cat")
dog_object = Animal("vegetarian dog")

cat_object.feed("fish")
cat_object.feed("chicken")

dog_object.feed("salad")
dog_object.feed("potatoes")

another_cat = Animal(cat_object)

another_cat.feed("milk")

cat_object.make_speak()
dog_object.make_speak()
another_cat.make_speak()
