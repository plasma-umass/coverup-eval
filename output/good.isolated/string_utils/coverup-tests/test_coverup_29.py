# file string_utils/validation.py:247-283
# lines [247, 269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283]
# branches ['269->270', '269->272', '272->273', '272->279', '273->274', '273->277', '279->280', '279->283', '280->279', '280->281']

import pytest
import re
from string_utils.validation import is_credit_card

# Assuming the CREDIT_CARDS dictionary is defined in the module where is_credit_card is defined.
# If not, this dictionary should be imported from the appropriate module.

def test_is_credit_card_invalid_type():
    with pytest.raises(KeyError) as exc_info:
        is_credit_card("4111111111111111", card_type="INVALID_CARD_TYPE")
    assert 'Invalid card type "INVALID_CARD_TYPE"' in str(exc_info.value)

def test_is_credit_card_valid_visa():
    assert is_credit_card("4111111111111111", card_type="VISA") == True

def test_is_credit_card_valid_mastercard():
    assert is_credit_card("5555555555554444", card_type="MASTERCARD") == True

def test_is_credit_card_valid_american_express():
    assert is_credit_card("378282246310005", card_type="AMERICAN_EXPRESS") == True

def test_is_credit_card_valid_diners_club():
    assert is_credit_card("30569309025904", card_type="DINERS_CLUB") == True

def test_is_credit_card_valid_discover():
    assert is_credit_card("6011111111111117", card_type="DISCOVER") == True

def test_is_credit_card_valid_jcb():
    assert is_credit_card("3530111333300000", card_type="JCB") == True

def test_is_credit_card_any_valid():
    assert is_credit_card("4111111111111111") == True

def test_is_credit_card_any_invalid():
    assert is_credit_card("1234567890123456") == False

def test_is_credit_card_empty_string():
    assert is_credit_card("") == False

def test_is_credit_card_none():
    assert is_credit_card(None) == False
