# Неправильно
class EventHandler:  # Обработчик событий
    def handle_event_1(self, event):
        # Обработчик первого события
        pass

    def handle_event_2(self, event):
        # Обработчик второго события
        pass

    def handle_event_3(self, event):
        # Обработчик третьего события
        pass

    def database_logger(self, event):
        # Метод для записи логов в базу данных
        pass


# Правильно
class EventHandler:  # Обработчик событий
    """
    Принцип единственной ответственности (The Single Responsibility Principle): у каждого
    объекта должна быть только одна ответственность. Все поведение этого объекта должно быть
    направлено на обеспечение этой ответственности и никаких других.
    """

    def handle_event_1(self, event):
        # Обработчик первого события
        pass

    def handle_event_2(self, event):
        # Обработчик второго события
        pass

    def handle_event_3(self, event):
        # Обработчик третьего события
        pass


class DatabaseLogger:

    def database_logger(self, event):
        # Метод для записи логов в базу данных
        pass
