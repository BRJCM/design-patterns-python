# Chain of Responsibility Pattern Example in Python
class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == 'A':
            return 'Handled by Handler 1'
        return super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == 'B':
            return 'Handled by Handler 2'
        return super().handle(request)

if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler1.set_next(handler2)

    print(handler1.handle('A'))  # Handled by Handler 1
    print(handler1.handle('B'))  # Handled by Handler 2
