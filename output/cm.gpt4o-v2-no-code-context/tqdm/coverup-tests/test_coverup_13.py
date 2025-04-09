# file: tqdm/notebook.py:101-147
# asked: {"lines": [101, 102, 114, 115, 116, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[114, 115], [114, 119], [119, 120], [119, 122], [125, 126], [125, 128], [130, 131], [130, 132], [134, 136], [134, 147], [138, 139], [138, 142]]}
# gained: {"lines": [101, 102, 114, 115, 116, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 147], "branches": [[114, 115], [114, 119], [119, 120], [119, 122], [125, 126], [130, 131], [134, 136], [134, 147], [138, 139]]}

import pytest
from unittest.mock import patch, MagicMock
from tqdm.notebook import tqdm_notebook

@pytest.fixture
def mock_ipywidgets():
    with patch('tqdm.notebook.IProgress', autospec=True) as mock_IProgress, \
         patch('tqdm.notebook.HTML', autospec=True) as mock_HTML, \
         patch('tqdm.notebook.TqdmHBox', autospec=True) as mock_TqdmHBox:
        yield mock_IProgress, mock_HTML, mock_TqdmHBox

def test_status_printer_no_total(mock_ipywidgets):
    mock_IProgress, mock_HTML, mock_TqdmHBox = mock_ipywidgets

    container = tqdm_notebook.status_printer(None, total=None, desc="Test", ncols=None)
    
    mock_IProgress.assert_called_once_with(min=0, max=1)
    assert mock_IProgress.return_value.value == 1
    assert mock_IProgress.return_value.bar_style == 'info'
    assert mock_IProgress.return_value.layout.width == "20px"
    assert mock_HTML.call_count == 2
    assert mock_TqdmHBox.call_count == 1
    assert container == mock_TqdmHBox.return_value

def test_status_printer_with_total(mock_ipywidgets):
    mock_IProgress, mock_HTML, mock_TqdmHBox = mock_ipywidgets

    container = tqdm_notebook.status_printer(None, total=100, desc="Test", ncols=None)
    
    mock_IProgress.assert_called_once_with(min=0, max=100)
    assert mock_HTML.call_count == 2
    assert mock_TqdmHBox.call_count == 1
    assert container == mock_TqdmHBox.return_value

def test_status_printer_with_ncols(mock_ipywidgets):
    mock_IProgress, mock_HTML, mock_TqdmHBox = mock_ipywidgets

    container = tqdm_notebook.status_printer(None, total=100, desc="Test", ncols=100)
    
    mock_IProgress.assert_called_once_with(min=0, max=100)
    assert mock_HTML.call_count == 2
    assert mock_TqdmHBox.call_count == 1
    assert container == mock_TqdmHBox.return_value
    assert container.layout.width == '100px'
    assert container.layout.display == 'inline-flex'
    assert container.layout.flex_flow == 'row wrap'

def test_status_printer_with_ncols_str(mock_ipywidgets):
    mock_IProgress, mock_HTML, mock_TqdmHBox = mock_ipywidgets

    container = tqdm_notebook.status_printer(None, total=100, desc="Test", ncols="50%")
    
    mock_IProgress.assert_called_once_with(min=0, max=100)
    assert mock_HTML.call_count == 2
    assert mock_TqdmHBox.call_count == 1
    assert container == mock_TqdmHBox.return_value
    assert container.layout.width == '50%'
    assert container.layout.display == 'inline-flex'
    assert container.layout.flex_flow == 'row wrap'

def test_status_printer_import_error():
    with patch('tqdm.notebook.IProgress', None):
        with pytest.raises(ImportError, match="IProgress not found. Please update jupyter and ipywidgets."):
            tqdm_notebook.status_printer(None, total=100, desc="Test", ncols=None)
