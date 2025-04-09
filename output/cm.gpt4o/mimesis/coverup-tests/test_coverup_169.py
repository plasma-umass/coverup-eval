# file mimesis/builtins/ru.py:50-64
# lines [60, 61, 63, 64]
# branches ['60->61', '60->63']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_passport_series_with_year(russia_spec_provider):
    year = 16
    series = russia_spec_provider.passport_series(year)
    assert series.endswith(f' {year}')
    region = int(series.split()[0])
    assert 1 <= region <= 99

def test_passport_series_without_year(russia_spec_provider, mocker):
    mock_random = mocker.patch.object(russia_spec_provider.random, 'randint', side_effect=[15, 42])
    series = russia_spec_provider.passport_series()
    assert series == '42 15'
    mock_random.assert_any_call(10, 18)
    mock_random.assert_any_call(1, 99)
