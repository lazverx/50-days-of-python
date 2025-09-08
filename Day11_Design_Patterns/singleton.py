class SingletonMeta(type):
    """A Singleton metaclass ensuring only one instance is created."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, conn_string):
        self.conn_string = conn_string


if __name__ == "__main__":
    db1 = DatabaseConnection("db://localhost")
    db2 = DatabaseConnection("db://remote")

    print(db1.conn_string)  # db://localhost
    print(db2.conn_string)  # db://localhost (same instance)
    print(db1 is db2)       # True
