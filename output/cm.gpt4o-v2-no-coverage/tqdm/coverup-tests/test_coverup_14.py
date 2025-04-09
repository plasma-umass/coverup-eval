# file: tqdm/notebook.py:76-94
# asked: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 93, 94], "branches": [[80, 81], [80, 82], [83, 84], [83, 85], [89, 90], [89, 91]]}
# gained: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 93, 94], "branches": [[80, 81], [80, 82], [83, 84], [83, 85], [89, 90], [89, 91]]}

import pytest
from unittest.mock import Mock, patch
from ipywidgets import HBox
from tqdm.notebook import TqdmHBox

@pytest.fixture
def mock_pbar():
    mock = Mock()
    mock.format_dict = {'n': 5, 'total': 10, 'elapsed': 1, 'ncols': 10}
    mock.format_meter = Mock(return_value="5/10 [00:01<00:00, 10.0it/s]")
    return mock

def test_tqdm_hbox_repr_json_no_pbar():
    hbox = TqdmHBox()
    assert hbox._repr_json_() == {}

def test_tqdm_hbox_repr_json_with_pbar(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    assert hbox._repr_json_() == mock_pbar.format_dict

def test_tqdm_hbox_repr_json_with_pretty(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    expected_dict = mock_pbar.format_dict.copy()
    expected_dict['ascii'] = False
    assert hbox._repr_json_(pretty=True) == expected_dict

def test_tqdm_hbox_repr_no_pbar():
    hbox = TqdmHBox()
    assert repr(hbox) == super(TqdmHBox, hbox).__repr__()

def test_tqdm_hbox_repr_with_pbar(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    assert repr(hbox) == "5/10 [00:01<00:00, 10.0it/s]"

def test_tqdm_hbox_repr_pretty(mock_pbar):
    hbox = TqdmHBox()
    hbox.pbar = mock_pbar
    pp = Mock()
    hbox._repr_pretty_(pp)
    pp.text.assert_called_once_with("5/10 [00:01<00:00, 10.0it/s]")
