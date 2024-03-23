# file mimesis/builtins/ru.py:77-88
# lines [77, 85, 86, 87]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_provider():
    return RussiaSpecProvider()

def test_series_and_number(russia_provider):
    result = russia_provider.series_and_number()
    assert len(result) == 11  # Assuming the series is 4 digits and number is 6 digits + space
    assert result[2] == ' '  # Assuming the space is after the 2nd character (series)
    assert result.isdigit() == False  # The result should not be all digits due to the space
    assert result.replace(' ', '').isdigit() == True  # The result without space should be all digits
