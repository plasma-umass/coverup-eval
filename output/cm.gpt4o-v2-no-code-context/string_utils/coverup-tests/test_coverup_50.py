# file: string_utils/validation.py:247-283
# asked: {"lines": [269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283], "branches": [[269, 270], [269, 272], [272, 273], [272, 279], [273, 274], [273, 277], [279, 280], [279, 283], [280, 279], [280, 281]]}
# gained: {"lines": [269, 270, 272, 273, 274, 275, 277, 279, 280, 281, 283], "branches": [[269, 270], [269, 272], [272, 273], [272, 279], [273, 274], [273, 277], [279, 280], [279, 283], [280, 279], [280, 281]]}

import pytest
from string_utils.validation import is_credit_card

def test_is_credit_card_invalid_string():
    assert not is_credit_card(None)
    assert not is_credit_card(1234567890123456)
    assert not is_credit_card("")

def test_is_credit_card_invalid_card_type():
    with pytest.raises(KeyError):
        is_credit_card("4111111111111111", "INVALID_CARD")

def test_is_credit_card_valid_card_type():
    assert is_credit_card("4111111111111111", "VISA")
    assert not is_credit_card("4111111111111111", "MASTERCARD")

def test_is_credit_card_any_card_type():
    assert is_credit_card("4111111111111111")
    assert is_credit_card("5500000000000004")
    assert not is_credit_card("1234567890123456")
