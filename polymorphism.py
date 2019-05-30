class Parent:
    """
    Парадигма полиморфизма позволяет вместо объекта базового типа использовать его потомка,
    при этом не указывая это явно.
    """
    def some_method(self):
        print("This is Parent object")


class Child1(Parent):

    def some_method(self):
        print("This is Child1 object")


class Child2(Parent):

    def some_method(self):
        print("This is Child2 object")


def who_am_i(obj):
    obj.some_method()


p = Parent()
c1 = Child1()
c2 = Child2()

who_am_i(p)
who_am_i(c1)
who_am_i(c2)
print()

# This is Parent object
# This is Child1 object
# This is Child2 object