# file: thonny/jedi_utils.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from unittest import mock

# Assuming the function _using_older_jedi is imported from thonny.jedi_utils
from thonny.jedi_utils import _using_older_jedi

def test_using_older_jedi_with_old_version():
    mock_jedi = mock.Mock()
    mock_jedi.__version__ = "0.14.1"
    assert _using_older_jedi(mock_jedi) == True

def test_using_older_jedi_with_new_version():
    mock_jedi = mock.Mock()
    mock_jedi.__version__ = "0.18.0"
    assert _using_older_jedi(mock_jedi) == False

def test_using_older_jedi_with_edge_case_version():
    mock_jedi = mock.Mock()
    mock_jedi.__version__ = "0.17.9"
    assert _using_older_jedi(mock_jedi) == True

def test_using_older_jedi_with_non_matching_version():
    mock_jedi = mock.Mock()
    mock_jedi.__version__ = "1.0.0"
    assert _using_older_jedi(mock_jedi) == False
