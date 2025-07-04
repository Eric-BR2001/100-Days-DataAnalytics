# User Registration Validation

This project provides a simple and extensible system for validating and registering users for an application. It includes utility functions to verify user input and handle registration logic safely and clearly.

## 📋 Features

* Validates user input for:

  * Name
  * Email
  * Password
* Raises descriptive errors for invalid input
* Safely handles registration logic
* Returns user details upon successful registration

## 🔧 Functions

### `validate_user(name, email, password)`

Validates user input using helper functions:

* `validate_name(name)`
* `validate_email(email)`
* `validate_password(password)`

**Behavior:**

* Raises `ValueError` with an appropriate message if any validation fails
* Returns `True` if all inputs are valid

### `register_user(name, email, password)`

Handles the registration process.

**Behavior:**

* Calls `validate_user()` to validate input
* If validation fails, catches the `ValueError` and returns `False`
* If validation succeeds, returns a dictionary with the user's details:

  ```python
  {
    "name": name,
    "email": email,
    "password": password
  }
  ```

