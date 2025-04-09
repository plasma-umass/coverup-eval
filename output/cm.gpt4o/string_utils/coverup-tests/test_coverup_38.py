# file string_utils/validation.py:247-283
# lines [247, 269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283]
# branches ['269->270', '269->272', '272->273', '272->279', '273->274', '273->277', '279->280', '279->283', '280->279', '280->281']

import re
import pytest
from string_utils.validation import is_credit_card

# Mock data for CREDIT_CARDS
CREDIT_CARDS = {
    'VISA': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MASTERCARD': re.compile(r'^5[1-5][0-9]{14}$'),
    'AMERICAN_EXPRESS': re.compile(r'^3[47][0-9]{13}$'),
    'DINERS_CLUB': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'DISCOVER': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^(?:2131|1800|35\d{3})\d{11}$')
}

def is_full_string(input_string):
    return isinstance(input_string, str) and bool(input_string.strip())

@pytest.mark.parametrize("input_string, card_type, expected", [
    ("4111111111111111", "VISA", True),  # Valid VISA
    ("5500000000000004", "MASTERCARD", True),  # Valid MasterCard
    ("340000000000009", "AMERICAN_EXPRESS", True),  # Valid AMEX
    ("30000000000004", "DINERS_CLUB", True),  # Valid Diners Club
    ("6011000000000004", "DISCOVER", True),  # Valid Discover
    ("3530111333300000", "JCB", True),  # Valid JCB
    ("4111111111111111", "MASTERCARD", False),  # Valid VISA but wrong type
    ("1234567890123456", None, False),  # Invalid card number
    ("", None, False),  # Empty string
    (None, None, False),  # None input
    ("4111111111111111", "INVALID_TYPE", False),  # Invalid card type
])
def test_is_credit_card(input_string, card_type, expected):
    if card_type == "INVALID_TYPE":
        with pytest.raises(KeyError):
            is_credit_card(input_string, card_type)
    else:
        assert is_credit_card(input_string, card_type) == expected
