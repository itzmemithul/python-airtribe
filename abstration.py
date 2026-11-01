from abc import ABC, abstractmethod

# Abstract class
# It is a class. And thus, it behaves like normal class.
# You cannot create a object of an abstract class. You can only create a reference of an abstract class.
# It can have abstract as well as non-abstract methods.

# Abstract method
# It is a method which is declared in an abstract class but has no function body.
# It must be overridden in the child class.

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine started.")

    def stop(self):
        print("Petrol engine stopped.")

class DieselEngine(Engine):
    def start(self):
        print("Diesel engine started.")

    def stop(self):
        print("Diesel engine stopped.")

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started.")

# engine = ElectricEngine()
# engine.start()  # Output: Electric engine started.
# engine.stop()   # Output: Electric engine stopped.

class HybridEngine(ElectricEngine, PetrolEngine):
    def start(self):
        print("Hybrid engine started.")
        ElectricEngine.start(self)

    # def stop(self):
    #     print("Hybrid engine stopped.")
    #     PetrolEngine.stop(self)
    #     ElectricEngine.stop(self)

engine = HybridEngine()
engine.start()  # Output: Hybrid engine started. Petrol engine started. Electric engine started.
engine.stop()   # Output: Hybrid engine stopped. Petrol engine stopped. Electric engine stopped.