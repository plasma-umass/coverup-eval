# file mimesis/providers/text.py:54-63
# lines [54, 60, 61, 62, 63]
# branches ['61->62', '61->63']

import pytest
from mimesis.providers.text import Text

@pytest.fixture
def text_provider():
    return Text()

def test_text_quantity(text_provider):
    # Test for quantity = 5 (default)
    result_default = text_provider.text()
    assert isinstance(result_default, str)
    assert len(result_default.split()) >= 5  # Assuming there's at least one word per sentence

    # Test for quantity = 10
    result_quantity_10 = text_provider.text(quantity=10)
    assert isinstance(result_quantity_10, str)
    assert len(result_quantity_10.split()) >= 10  # Assuming there's at least one word per sentence

    # Test for quantity = 0
    result_quantity_0 = text_provider.text(quantity=0)
    assert result_quantity_0 == ''  # Should return an empty string

    # Test for quantity = 1
    result_quantity_1 = text_provider.text(quantity=1)
    assert isinstance(result_quantity_1, str)
    assert len(result_quantity_1.split()) >= 1  # Assuming there's at least one word per sentence

    # The original code does not raise a ValueError for negative quantities,
    # so we remove the test case that expects a ValueError.
