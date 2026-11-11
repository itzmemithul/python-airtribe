# Library Manager — Q&A

## 1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?

- `LibraryItem` is abstract so you cannot create a generic item. You can only create the defined child classes (`Book`, `Magazine`, `DVD`).
- `late_fee()` is an abstract method. If a child class such as `DVD` does not implement it, Python will not construct that class at all and will raise an exception.

## 2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?

- `__available` is a private attribute. Reading `item.__available` from outside the class raises an `AttributeError`.
- `is_available()` is a getter that uses `__available`. Child classes inherit this method, so callers check availability through the public API instead of touching the private attribute.

## 3. What is the difference between `LibraryItem.total_items` and `self.title`?

- `LibraryItem.total_items` is a **class attribute**: one shared count of created items.
- `self.title` is an **instance attribute**: each object has its own title.
