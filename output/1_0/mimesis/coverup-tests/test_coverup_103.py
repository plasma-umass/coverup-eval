# file mimesis/providers/code.py:97-103
# lines [97, 103]
# branches []

import pytest
from mimesis.providers.code import Code

@pytest.fixture
def code_provider():
    return Code()

def test_pin_code(code_provider):
    pin = code_provider.pin()
    assert len(pin) == 4, "The pin should be 4 characters long"
    assert pin.isdigit(), "The pin should contain only digits"
    pin_with_custom_mask = code_provider.pin(mask='##-##')
    assert len(pin_with_custom_mask) == 5, "The pin with custom mask should be 5 characters long"
    assert pin_with_custom_mask[2] == '-', "The pin with custom mask should contain a hyphen as a separator"
