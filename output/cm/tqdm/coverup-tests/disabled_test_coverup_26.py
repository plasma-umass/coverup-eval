# file tqdm/rich.py:129-139
# lines [137, 138, 139]
# branches ['137->138', '137->139']

import pytest
from tqdm.rich import tqdm_rich
from unittest.mock import Mock, patch

@pytest.fixture
def mock_prog():
    mock = Mock()
    mock.reset = Mock()
    return mock

def test_tqdm_rich_reset_with_prog_attr(mock_prog):
    # Create an instance of tqdm_rich and manually add the _prog attribute
    tr = tqdm_rich(total=100)
    tr._prog = mock_prog

    # Call the reset method
    tr.reset(total=50)

    # Check if the _prog.reset method was called with the correct total
    mock_prog.reset.assert_called_once_with(total=50)

    # Clean up by removing the _prog attribute
    del tr._prog

    # Check if the super().reset method was called with the correct total
    with patch.object(tqdm_rich, 'reset', wraps=tr.reset) as mock_reset:
        tr.reset(total=50)
        mock_reset.assert_called_with(total=50)
