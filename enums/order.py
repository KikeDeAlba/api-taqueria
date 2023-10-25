from enum import Enum

class Status(Enum):
    pending = 1
    canceled = 2
    payed = 3

class TypeOrder(Enum):
    domicilio = 1
    comenzal = 2