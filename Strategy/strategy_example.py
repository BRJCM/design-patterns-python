# Strategy Pattern Example in Python
class Context:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

class Strategy:
    def execute(self, a, b):
        pass

class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b

if __name__ == "__main__":
    context = Context()
    context.set_strategy(ConcreteStrategyAdd())
    print(context.execute_strategy(2, 3))  # 5
    context.set_strategy(ConcreteStrategyMultiply())
    print(context.execute_strategy(2, 3))  # 6
