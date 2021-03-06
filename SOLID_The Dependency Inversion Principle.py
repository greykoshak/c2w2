"""
Принцип инверсии зависимостей (The Dependency Inversion Principle):

Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны
зависеть от абстракций.
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
Приведем пример. Пусть у вас есть базовый класс Distributer, который может отправлять сообщения
в различные социальные сети. У этого класса есть несколько реализаций, например VKDistributer и
OKDistributer. Согласно принципу инверсии зависимостей, эти реализации не должны зависеть от
методов класса Distributer (например VK_send_message и OK_send_message). Вместо этого у
класса Destributor должен быть объявлен общий абстрактный метод send_message, который и будет
реализован отдельно в каждом из потомков.


"""