class Parent:
    
    def __init__(self, name):
        self.name = name

    def test_function(self):
        print("This is a test function in the Parent class.")

class Child(Parent):
    def my_function(self):
        print("This is a method in the Child class.")

    def test_function(self): # this is called function overriding. The test_function of the Parent class is overridden in the Child class.
        print("This is a test function in the Child class.")

    def parent_test_function(self):
        super().test_function() # this is how we can call the test_function of the Parent class from the Child class.

# c1 = Child("Rushika")
# c1.test_function()
c2 = Child("Rushika")
c2.my_function()
c2.test_function()
c2.parent_test_function()