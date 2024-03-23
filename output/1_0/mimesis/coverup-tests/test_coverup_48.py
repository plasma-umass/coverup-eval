# file mimesis/providers/code.py:31-34
# lines [31, 32, 34]
# branches []

import pytest
from mimesis.providers.code import Code
from mimesis import Generic

@pytest.fixture
def code_provider():
    return Code()

def test_code_meta_class(code_provider):
    assert code_provider.Meta.name == 'code'
