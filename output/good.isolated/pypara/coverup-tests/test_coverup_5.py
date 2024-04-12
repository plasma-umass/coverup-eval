# file pypara/dcc.py:176-188
# lines [176, 180, 181, 182, 183, 184, 185, 186, 188]
# branches ['180->181', '180->182', '185->186', '185->188']

import pytest
import datetime
from pypara.dcc import _construct_date

def test_construct_date_with_invalid_values():
    with pytest.raises(ValueError) as exc_info:
        _construct_date(0, 1, 1)
    assert str(exc_info.value) == "year, month and day must be greater than 0."

    with pytest.raises(ValueError) as exc_info:
        _construct_date(2023, 0, 1)
    assert str(exc_info.value) == "year, month and day must be greater than 0."

    with pytest.raises(ValueError) as exc_info:
        _construct_date(2023, 1, 0)
    assert str(exc_info.value) == "year, month and day must be greater than 0."

def test_construct_date_with_day_out_of_range():
    # February 29th on a non-leap year
    result = _construct_date(2023, 2, 29)
    assert result == datetime.date(2023, 2, 28)

def test_construct_date_with_valid_values():
    result = _construct_date(2023, 1, 1)
    assert result == datetime.date(2023, 1, 1)
