# file mimesis/providers/choice.py:15-18
# lines [15, 16, 18]
# branches []

import pytest
from mimesis.providers.choice import Choice

def test_choice_meta():
    choice_provider = Choice()
    assert choice_provider.Meta.name == 'choice'
