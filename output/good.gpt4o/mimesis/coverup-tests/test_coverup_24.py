# file mimesis/builtins/pl.py:25-40
# lines [25, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40]
# branches ['37->38', '37->39']

import pytest
from mimesis.builtins.pl import PolandSpecProvider

@pytest.fixture
def poland_spec_provider():
    return PolandSpecProvider()

def test_nip(poland_spec_provider, mocker):
    # Mock the random.randint method to control the output
    mocker.patch.object(poland_spec_provider.random, 'randint', side_effect=[101, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    nip = poland_spec_provider.nip()
    
    # Assert the length of the NIP is 10 digits
    assert len(nip) == 10
    
    # Assert the NIP is composed of digits only
    assert nip.isdigit()
    
    # Assert the first three digits are the mocked values
    assert nip.startswith('101')
    
    # Assert the checksum digit is correctly calculated
    nip_digits = [int(d) for d in nip]
    nip_coefficients = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    sum_v = sum([nc * nd for nc, nd in zip(nip_coefficients, nip_digits[:-1])])
    checksum_digit = sum_v % 11
    assert nip_digits[-1] == checksum_digit

def test_nip_checksum_greater_than_9(poland_spec_provider, mocker):
    # Mock the random.randint method to control the output
    mocker.patch.object(poland_spec_provider.random, 'randint', side_effect=[998, 9, 9, 9, 9, 9, 9, 9, 9, 9])

    nip = poland_spec_provider.nip()
    
    # Assert the length of the NIP is 10 digits
    assert len(nip) == 10
    
    # Assert the NIP is composed of digits only
    assert nip.isdigit()
    
    # Assert the first three digits are the mocked values
    assert nip.startswith('998')
    
    # Assert the checksum digit is correctly calculated
    nip_digits = [int(d) for d in nip]
    nip_coefficients = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    sum_v = sum([nc * nd for nc, nd in zip(nip_coefficients, nip_digits[:-1])])
    checksum_digit = sum_v % 11
    if checksum_digit > 9:
        checksum_digit = sum([nc * nd for nc, nd in zip(nip_coefficients, nip_digits[:-1])]) % 11
    assert nip_digits[-1] == checksum_digit
