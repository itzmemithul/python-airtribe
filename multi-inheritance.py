class ParentOne:
    def test_function(self):
        print("This is parent one test function")
    def parent_one_function(self):
        print("This is parent one function")

class ParentTwo:
    def test_function(self):
        print("This is parent two test function")
    def parent_two_function(self):
        print("This is parent two function")

class Child(ParentTwo, ParentOne):
    pass

c1 = Child()
c1.test_function()  # This will call the method from ParentTwo
c1.parent_one_function()  # This will call the method from ParentOne
c1.parent_two_function()  # This will call the method from ParentTwo