# file mimesis/providers/numbers.py:95-124
# lines [95, 96, 97, 98, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 124]
# branches ['113->114', '113->124']

import pytest
from mimesis.providers.numbers import Numbers

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_complexes(numbers_provider):
    start_real = 1.0
    end_real = 2.0
    start_imag = 1.0
    end_imag = 2.0
    precision_real = 2
    precision_imag = 2
    n = 5

    result = numbers_provider.complexes(
        start_real=start_real,
        end_real=end_real,
        start_imag=start_imag,
        end_imag=end_imag,
        precision_real=precision_real,
        precision_imag=precision_imag,
        n=n
    )

    assert len(result) == n
    for complex_number in result:
        assert start_real <= complex_number.real <= end_real
        assert start_imag <= complex_number.imag <= end_imag
        assert len(str(complex_number.real).split('.')[1]) <= precision_real
        assert len(str(complex_number.imag).split('.')[1]) <= precision_imag
