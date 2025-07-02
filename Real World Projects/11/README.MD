# Core Sign-Up Validation Functions

This project focuses on building foundational Python functions to validate user input during the sign-up process. It includes custom functions to ensure that names and emails entered by users meet basic validation criteria.

## Features

- **`validate_name()`**
  - Checks if the provided name is a valid string.
  - Ensures the name is longer than two characters.
  - Returns `True` if the name is valid, otherwise returns `False`.

- **`validate_email()`**
  - Validates that the email contains an `@` symbol.
  - Confirms that the email ends with a recognized top-level domain (TLD), using a preloaded `top_level_domains` list.
  - Returns `True` if the email is valid, otherwise returns `False`.

## Usage

You can import and use the functions in any Python project that requires user input validation.

### Example

```python
from validation import validate_name, validate_email

print(validate_name("Eric"))        # True
print(validate_name("Al"))          # False
print(validate_email("user@example.com"))  # True
print(validate_email("invalidemail"))      # False