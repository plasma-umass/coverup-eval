# file mimesis/providers/text.py:26-29
# lines [26, 27, 29]
# branches []

import pytest
from mimesis.providers.text import Text

def test_text_meta_name():
    text_provider = Text()
    assert text_provider.Meta.name == 'text'
