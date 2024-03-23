# file mimesis/providers/code.py:88-95
# lines [93, 94, 95]
# branches []

import pytest
from mimesis.providers.code import Code
from mimesis.providers.base import BaseProvider
from mimesis.random import Random
from unittest.mock import patch

# Mocking the IMEI_TACS constant for the purpose of the test
IMEI_TACS = ['490154', '490154']

# Mocking the luhn_checksum function for the purpose of the test
def mock_luhn_checksum(num):
    return '7'

@pytest.fixture
def code_provider():
    return Code()

def test_imei(code_provider):
    with patch('mimesis.providers.code.IMEI_TACS', IMEI_TACS):
        with patch('mimesis.providers.code.luhn_checksum', mock_luhn_checksum):
            imei = code_provider.imei()
            assert imei.startswith(tuple(IMEI_TACS))
            assert imei[-1] == mock_luhn_checksum(imei[:-1])
            assert len(imei) == len(IMEI_TACS[0]) + 6 + 1  # TAC + Serial Number + Checksum
