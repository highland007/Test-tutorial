# Test classes

from xmlrpc.server import DocCGIXMLRPCRequestHandler


class Dog:

    kind = "canine"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

class Employee:
    pass


d = Dog("Fido")
e = Dog("Bobby")

print(d.name, d.kind, d.tricks)
print(e.name, e.kind, e.tricks)

d.add_trick("roll over")
e.add_trick("jump")

print(d.name, d.kind, d.tricks)
print(e.name, e.kind, e.tricks)

emp1 = Employee()
emp1.name = "John"
emp1.dept = "RD"

print(emp1.name, emp1.dept)

