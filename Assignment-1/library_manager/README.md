Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
- LibraryItem is abstract because it doesn't let us create a generic item apart from the ones that are already defined as child classes.
- Since late_fee() is an abstract method in itself if it is not used in the child class of LibraryItem it would not construct the DVD class at all throwing an exception.
What happens when you read item.__available from outside the class, and why do we use is_available() instead?
- item.__available is a private variable and reading it outside the class would throw an attribute error
- is_available is a getter which uses the __available and comes in as a method that can be shared across child classes.
What is the difference between LibraryItem.total_items and self.title?
- LibraryItem.total_items is a class attribute: one shared count of created items. self.title is an instance attribute: each object has its own title.