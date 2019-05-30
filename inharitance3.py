"""
Множественное наследование позволяет получить доступ к атрибутам нескольких родительских классов:
"""

class A:

    def some_function(self):
        print("First function")

    def other_function(self):
        print("Second function")


class B:

    def method_in_B(self):
        print("Third function")


class С(A, B):
    pass


# Посмотрим все атрибуты класса, не являющиеся служебными
print("A:\t", list(filter(lambda x: "__" not in x, dir(A))))
print("B:\t", list(filter(lambda x: "__" not in x, dir(B))))
print("С(A,B):\t", list(filter(lambda x: "__" not in x, dir(С))))
print()

# A:	 ['other_function', 'some_function']
# B:	 ['method_in_B']
# С(A,B):	 ['method_in_B', 'other_function', 'some_function']

