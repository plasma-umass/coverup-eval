# file: tqdm/notebook.py:76-94
# asked: {"lines": [79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 91, 94], "branches": [[80, 81], [80, 82], [83, 84], [83, 85], [89, 90], [89, 91]]}
# gained: {"lines": [79, 80, 81, 82, 83, 84, 85, 88, 89, 90, 91, 94], "branches": [[80, 81], [80, 82], [83, 84], [83, 85], [89, 90], [89, 91]]}

import pytest
from unittest.mock import MagicMock
from ipywidgets import HBox
from tqdm.notebook import TqdmHBox

@pytest.fixture
def mock_pbar():
    mock = MagicMock()
    mock.format_dict = {'value': 42}
    mock.format_meter = MagicMock(return_value="formatted_meter")
    return mock

def test_repr_json_with_pbar(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    result = hbox._repr_json_()
    assert result == {'value': 42}

def test_repr_json_without_pbar():
    hbox = TqdmHBox()
    result = hbox._repr_json_()
    assert result == {}

def test_repr_json_with_pretty(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    result = hbox._repr_json_(pretty=True)
    assert result == {'value': 42, 'ascii': False}

def test_repr_with_pbar(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    result = hbox.__repr__()
    assert result == "formatted_meter"

def test_repr_without_pbar():
    hbox = TqdmHBox()
    result = hbox.__repr__()
    assert result == super(TqdmHBox, hbox).__repr__()

def test_repr_pretty(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    pp = MagicMock()
    hbox._repr_pretty_(pp)
    pp.text.assert_called_once_with("formatted_meter")
