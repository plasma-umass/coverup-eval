# file mimesis/builtins/ru.py:50-64
# lines [50, 60, 61, 63, 64]
# branches ['60->61', '60->63']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.random import Random

@pytest.fixture
def russia_spec_provider(mocker):
    mocker.patch('mimesis.random.Random', return_value=Random())
    return RussiaSpecProvider()

def test_passport_series_with_year(russia_spec_provider):
    year = 16
    series = russia_spec_provider.passport_series(year=year)
    assert len(series) == 5
    assert series.endswith(str(year))

def test_passport_series_without_year(russia_spec_provider):
    series = russia_spec_provider.passport_series()
    assert len(series) == 5
    assert series[2] == ' '
    assert 10 <= int(series[3:]) <= 18
