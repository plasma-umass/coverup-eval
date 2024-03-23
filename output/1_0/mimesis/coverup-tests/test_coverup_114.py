# file mimesis/providers/code.py:46-52
# lines [52]
# branches []

import pytest
from mimesis.providers.code import Code

@pytest.fixture
def code_provider():
    return Code()

def test_issn_with_custom_mask(code_provider, mocker):
    custom_mask = '##-##-####'
    mocker.patch.object(code_provider.random, 'custom_code', return_value="1234-5678")
    issn = code_provider.issn(mask=custom_mask)
    assert issn == "1234-5678", "ISSN does not match the expected output"
