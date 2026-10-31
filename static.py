class Demo:

    #static variable
    a = 5

    def __init__(self, b):
        self.b = b

    def test_function(self):
        print("This is a test function in the Demo class.")

    @staticmethod
    def my_function():
        print("This is a static method in the Demo class.")

print(Demo.a) # While access the static variable we don't need to create an object of the class. We can access it directly using the class name.
d1 = Demo(10) # Creating an object of the class Demo, here 10 is passed as an argument to the constructor and assigned to the instance variable b.
print(d1.a) # Accessing the instance variable a using the object d1. 
d1.a = 50
print(d1.a) # Accessing the instance variable a using the object d1 after modifying it. 
'''Static variable cannot be modified using the object of the class. It can only be modified using the class name. 
In case if we try to modify the static variable using the object of the class, it will create a new instance variable with the same name.'''