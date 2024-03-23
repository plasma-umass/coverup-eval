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
    assert len(result_default.split()) >= 5  # Assuming there are at least 5 words in the sentences

    # Test for quantity = 10
    result_quantity_10 = text_provider.text(quantity=10)
    assert isinstance(result_quantity_10, str)
    assert len(result_quantity_10.split()) >= 10  # Assuming there are at least 10 words in the sentences

    # Test for quantity = 0
    result_quantity_0 = text_provider.text(quantity=0)
    assert result_quantity_0 == ''  # Should return an empty string

    # Test for quantity = 1
    result_quantity_1 = text_provider.text(quantity=1)
    assert isinstance(result_quantity_1, str)
    assert len(result_quantity_1.split()) >= 1  # Assuming there is at least 1 word in the sentence

    # Test for quantity = -1 (should not generate any text)
    result_negative_quantity = text_provider.text(quantity=-1)
    assert result_negative_quantity == ''  # Should return an empty string

    # Test for quantity = 2 (to ensure loop runs more than once)
    result_quantity_2 = text_provider.text(quantity=2)
    assert isinstance(result_quantity_2, str)
    assert len(result_quantity_2.split()) >= 2  # Assuming there are at least 2 words in the sentences
