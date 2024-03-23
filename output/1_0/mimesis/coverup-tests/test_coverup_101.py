# file mimesis/providers/science.py:73-82
# lines [73, 82]
# branches []

import pytest
from mimesis.providers.science import Science

@pytest.fixture
def science_provider():
    return Science()

def test_dna_sequence(science_provider):
    # Test the default length of 10
    sequence = science_provider.dna_sequence()
    assert len(sequence) == 10
    assert set(sequence).issubset(set('TCGA'))

    # Test a custom length of 20
    custom_length_sequence = science_provider.dna_sequence(length=20)
    assert len(custom_length_sequence) == 20
    assert set(custom_length_sequence).issubset(set('TCGA'))

    # Test a length of 0
    empty_sequence = science_provider.dna_sequence(length=0)
    assert empty_sequence == ''

    # The original code does not raise a ValueError for negative lengths,
    # so we remove the incorrect test case.
