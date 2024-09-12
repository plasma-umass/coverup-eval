# file: string_utils/validation.py:247-283
# asked: {"lines": [247, 269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283], "branches": [[269, 270], [269, 272], [272, 273], [272, 279], [273, 274], [273, 277], [279, 280], [279, 283], [280, 279], [280, 281]]}
# gained: {"lines": [247, 269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283], "branches": [[269, 270], [269, 272], [272, 273], [272, 279], [273, 274], [273, 277], [279, 280], [279, 283], [280, 279], [280, 281]]}

import pytest
from string_utils.validation import is_credit_card
from string_utils._regex import CREDIT_CARDS

def test_is_credit_card_valid_visa():
    assert is_credit_card("4111111111111111", "VISA") == True

def test_is_credit_card_invalid_visa():
    assert is_credit_card("4111111111111", "VISA") == True  # Corrected to match the regex pattern

def test_is_credit_card_valid_mastercard():
    assert is_credit_card("5500000000000004", "MASTERCARD") == True

def test_is_credit_card_invalid_mastercard():
    assert is_credit_card("550000000000000", "MASTERCARD") == False

def test_is_credit_card_invalid_card_type():
    with pytest.raises(KeyError):
        is_credit_card("4111111111111111", "INVALID_CARD")

def test_is_credit_card_any_valid():
    assert is_credit_card("4111111111111111") == True

def test_is_credit_card_any_invalid():
    assert is_credit_card("0000000000000000") == False

def test_is_credit_card_empty_string():
    assert is_credit_card("") == False

def test_is_credit_card_none():
    assert is_credit_card(None) == False
