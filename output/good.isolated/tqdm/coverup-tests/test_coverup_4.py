# file tqdm/rich.py:142-147
# lines [142, 147]
# branches []

import pytest
from tqdm.rich import tqdm_rich, trrange

# Mocking _range to control its behavior
@pytest.fixture
def mock_range(mocker):
    return mocker.patch('tqdm.rich._range', return_value=range(10))

# Test function to cover trrange
def test_trrange(mock_range):
    # Call trrange to ensure the tqdm_rich function is called with the mocked range
    progress_bar = trrange(10)
    
    # Assertions to verify postconditions
    assert mock_range.called, "The _range function should be called"
    assert mock_range.call_args[0] == (10,), "The _range function should be called with argument 10"
    assert isinstance(progress_bar, tqdm_rich), "trrange should return an instance of tqdm_rich"
    
    # Clean up is handled by pytest's fixture scope
