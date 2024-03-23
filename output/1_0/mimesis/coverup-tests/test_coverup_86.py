# file mimesis/providers/science.py:62-71
# lines [62, 71]
# branches []

import pytest
from mimesis.providers.science import Science

@pytest.fixture
def science_provider():
    return Science()

def test_rna_sequence(science_provider):
    sequence = science_provider.rna_sequence(10)
    assert len(sequence) == 10
    assert set(sequence).issubset(set('UCGA'))

    sequence_with_custom_length = science_provider.rna_sequence(20)
    assert len(sequence_with_custom_length) == 20
    assert set(sequence_with_custom_length).issubset(set('UCGA'))
