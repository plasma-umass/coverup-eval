# file tqdm/rich.py:24-46
# lines [36, 37, 38, 39]
# branches ['35->36']

import pytest
from tqdm.rich import FractionColumn
from rich.progress import Task
from rich.text import Text
from unittest.mock import Mock

# Mock the filesize.pick_unit_and_suffix function
@pytest.fixture
def mock_filesize_pick_unit_and_suffix(mocker):
    mock = mocker.patch('tqdm.rich.filesize.pick_unit_and_suffix', return_value=(1000000000, 'G'))
    return mock

# Test to cover lines 36-39
def test_fraction_column_render_with_unit_scale(mock_filesize_pick_unit_and_suffix):
    # Create a FractionColumn with unit_scale=True
    column = FractionColumn(unit_scale=True, unit_divisor=1000)
    # Create a mock task with completed and total values
    task = Task(id=0, description='', total=2300000000, completed=500000000, _get_time=lambda: 0)
    # Render the column with the mock task
    rendered = column.render(task)
    # Assert that the mock was called with the expected arguments
    mock_filesize_pick_unit_and_suffix.assert_called_once_with(
        2300000000, ["", "K", "M", "G", "T", "P", "E", "Z", "Y"], 1000
    )
    # Assert that the rendered text is as expected
    assert isinstance(rendered, Text)
    assert rendered.plain == "0.5/2.3 G"
