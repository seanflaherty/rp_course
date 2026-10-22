from collections import namedtuple
from datetime import date

_BasePerson = namedtuple("BasePerson", "name birth country", defaults=["Canada", ])

class PersonTuple(_BasePerson):
    """A namedtuple subclass representing a person"""
    __slots__ = ()

    def __repr__(self):
        return f"Name: {self.name}, age: {self.age} years old"
    
    @property
    def age(self):
        return (date.today() - self.birth).days // 365