# file typesystem/schemas.py:133-140
# lines [133, 134, 135, 136, 137, 138, 139]
# branches []

import pytest
from typesystem import Schema, Field
from typesystem.fields import Integer, String

# Define a custom schema to be used in the test
class CustomSchema(Schema):
    id = Integer()
    name = String(default="")

# Define the test function
def test_make_validator_strict_mode():
    # Create the validator with strict mode enabled
    validator_strict = CustomSchema.make_validator(strict=True)
    # Assert that additional_properties is False in strict mode
    assert validator_strict.additional_properties is False

    # Create the validator with strict mode disabled
    validator_non_strict = CustomSchema.make_validator(strict=False)
    # Assert that additional_properties is None when not in strict mode
    assert validator_non_strict.additional_properties is None

    # Assert that 'id' is in the required list as it does not have a default
    assert 'id' in validator_strict.required
    # Assert that 'name' is not in the required list as it has a default
    assert 'name' not in validator_strict.required

# Run the test function if this script is executed directly (not recommended)
if __name__ == "__main__":
    pytest.main()
