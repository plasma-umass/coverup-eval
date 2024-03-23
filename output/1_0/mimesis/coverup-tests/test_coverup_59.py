# file mimesis/providers/code.py:71-86
# lines [71, 81, 82, 83, 85, 86]
# branches []

import pytest
from mimesis.enums import EANFormat
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.code import Code

def test_ean_with_valid_format(mocker):
    # Setup
    provider = Code()
    mocker.patch.object(provider.random, 'custom_code', return_value='1234567890128')

    # Test EAN-13 format
    ean13 = provider.ean(fmt=EANFormat.EAN13)
    assert provider.random.custom_code.called
    assert ean13 == '1234567890128'

    # Test EAN-8 format
    provider.random.custom_code.reset_mock()
    ean8 = provider.ean(fmt=EANFormat.EAN8)
    assert provider.random.custom_code.called
    assert ean8 == '1234567890128'

def test_ean_with_invalid_format():
    provider = Code()
    with pytest.raises(NonEnumerableError):
        provider.ean(fmt='invalid_format')
