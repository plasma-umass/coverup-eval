# file mimesis/builtins/ru.py:77-88
# lines [77, 85, 86, 87]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_series_and_number(russia_spec_provider):
    result = russia_spec_provider.series_and_number()
    assert len(result) == 11  # Assuming the series is 4 chars and number is 6 chars + space
    assert result[2] == ' '  # Assuming the space is after the 2nd character of the series
    assert result.isdigit() == False  # There should be a space, so it's not all digits
    assert result.replace(' ', '').isdigit() == True  # Without spaces, it should be all digits
