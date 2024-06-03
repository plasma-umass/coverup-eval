# file tqdm/rich.py:49-72
# lines [59, 60, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72]
# branches ['60->61', '60->62', '62->63', '62->69']

import pytest
from rich.progress import Progress, Task
from rich.text import Text
from tqdm.rich import RateColumn
from unittest.mock import Mock

@pytest.fixture
def mock_task():
    task = Mock(spec=Task)
    return task

def test_rate_column_no_speed(mock_task):
    rate_column = RateColumn(unit="B")
    mock_task.speed = None
    result = rate_column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "? B/s"

def test_rate_column_with_speed_no_unit_scale(mock_task):
    rate_column = RateColumn(unit="B", unit_scale=False)
    mock_task.speed = 1500
    result = rate_column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "1,500 B/s"

def test_rate_column_with_speed_with_unit_scale(mock_task):
    rate_column = RateColumn(unit="B", unit_scale=True, unit_divisor=1000)
    mock_task.speed = 1500
    result = rate_column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "1.5 KB/s"

def test_rate_column_with_speed_with_unit_scale_custom_divisor(mock_task):
    rate_column = RateColumn(unit="B", unit_scale=True, unit_divisor=1024)
    mock_task.speed = 2048
    result = rate_column.render(mock_task)
    assert isinstance(result, Text)
    assert result.plain == "2.0 KB/s"
