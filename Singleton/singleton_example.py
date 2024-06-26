# Singleton Pattern Example in Python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

if __name__ == "__main__":
    instance1 = Singleton()
    instance2 = Singleton()
    print(instance1 is instance2)  # True
