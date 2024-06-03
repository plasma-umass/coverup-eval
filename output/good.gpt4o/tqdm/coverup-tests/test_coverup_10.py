# file tqdm/rich.py:24-46
# lines [24, 25, 26, 27, 28, 29, 31, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44, 45, 46]
# branches ['35->36', '35->42']

import pytest
from rich.progress import Progress, Task
from rich.text import Text
from tqdm.rich import FractionColumn

@pytest.fixture
def mock_task():
    def get_time():
        return None

    return Task(
        id=1,
        description="Test Task",
        total=2300,
        completed=500,
        fields={},
        visible=True,
        _get_time=get_time,
    )

def test_fraction_column_no_unit_scale(mock_task):
    column = FractionColumn(unit_scale=False)
    result = column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "500/2,300 "

def test_fraction_column_with_unit_scale(mock_task):
    column = FractionColumn(unit_scale=True, unit_divisor=1000)
    result = column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "0.5/2.3 K"

def test_fraction_column_with_different_unit_divisor(mock_task):
    column = FractionColumn(unit_scale=True, unit_divisor=1024)
    result = column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "0.5/2.2 K"
