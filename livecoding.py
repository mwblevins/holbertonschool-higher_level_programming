#!/usr/bin/python3
"""Example for Inheritance by Aaron"""

#OOP = Modularity, productivity, upgradeable which also means scalable#
#all classes are a subclass of Object = Inheritance#
#simple inheritance (majority of type in Holberton Python) = a single inheritance path/chain#
#the following is an example of Simple Inheritance#
class Parent(object):
    """respect your elders"""
    
    def __init__(self, name=None, age=None):
        """initializes the obj"""
        
        self.name = name
        self.age = age
        
    def speak(self, phrase='Im alive'):
        """Speaking method"""
        
        print(phrase)
        
class Child(Parent):
    """Doesnt respect"""
    
    def __init__(self, name=None, age=None):
        super().__init__(name, age)