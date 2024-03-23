# file mimesis/builtins/ru.py:50-64
# lines [50, 60, 61, 63, 64]
# branches ['60->61', '60->63']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis import Generic

@pytest.fixture
def russia_provider():
    generic = Generic('ru')
    return RussiaSpecProvider(generic)

def test_passport_series_with_year(russia_provider):
    year = 16
    series = russia_provider.passport_series(year=year)
    assert len(series) == 5
    assert series.endswith(str(year))

def test_passport_series_without_year(russia_provider):
    series = russia_provider.passport_series()
    assert len(series) == 5
    assert int(series.split(' ')[1]) in range(10, 19)
