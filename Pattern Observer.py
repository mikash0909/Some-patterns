from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, note):  # Абстрактный наблюдатель задает метод update
        pass
class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements=set()
    def update(self, note): # Конкретная реализация метода update
        self.achievements.add(note['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, note):  # Конкретная реализация метода update
        if note not in self.achievements:
            self.achievements.append(note)