# file mimesis/providers/generic.py:66-69
# lines [66, 67, 69]
# branches []

import pytest
from mimesis.providers.generic import Generic

def test_generic_meta():
    generic = Generic()
    assert generic.Meta.name == 'generic'
