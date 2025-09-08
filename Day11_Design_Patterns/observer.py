class Observer:
    def update(self, message: str):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received: {message}")


if __name__ == "__main__":
    subject = Subject()

    alice = User("Alice")
    bob = User("Bob")

    subject.attach(alice)
    subject.attach(bob)

    subject.notify("New blog post available!")
