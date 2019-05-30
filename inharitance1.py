"""
Наследование — одна из самых важных и мощных парадигм ООП. При наследовании мы оперируем
такими понятиями, как родительский класс и класс потомок. Класс-потомок наследует методы и
переменные, определенные в родительском классе. Рассмотрим на примере:
"""

class A:
    var_A = 1

    def method_A(self):
        print("A")


class B(A):
    var_B = 2

    def method_B(self):
        print("B")


class C(B):
    var_C = 3

    def method_C(self):
        print("C")


print("A:\t", list(filter(lambda x: "__" not in x, dir(A))))
print("B(A):\t", list(filter(lambda x: "__" not in x, dir(B))))
print("C(B):\t", list(filter(lambda x: "__" not in x, dir(C))))
print()

# A:	 ['method_A', 'var_A']
# B(A):	 ['method_A', 'method_B', 'var_A', 'var_B']
# C(B):	 ['method_A', 'method_B', 'method_C', 'var_A', 'var_B', 'var_C']