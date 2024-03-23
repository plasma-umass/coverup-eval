# file mimesis/enums.py:59-67
# lines [59, 60, 65, 66, 67]
# branches []

import pytest
from mimesis.enums import CardType

def test_card_type_enum():
    assert CardType.MASTER_CARD.value == 'MasterCard'
    assert CardType.VISA.value == 'Visa'
    assert CardType.AMERICAN_EXPRESS.value == 'American Express'
