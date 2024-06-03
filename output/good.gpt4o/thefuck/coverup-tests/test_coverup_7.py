# file thefuck/rules/brew_install.py:9-19
# lines [9, 11, 12, 13, 15, 16, 17, 18, 19]
# branches ['15->exit', '15->16', '16->15', '16->17']

import os
import pytest
from unittest import mock
from thefuck.rules.brew_install import _get_formulas

@pytest.fixture
def mock_get_brew_path_prefix(mocker):
    return mocker.patch('thefuck.rules.brew_install.get_brew_path_prefix')

def test_get_formulas_success(mock_get_brew_path_prefix, mocker):
    mock_get_brew_path_prefix.return_value = '/mocked/path'
    mocker.patch('os.listdir', return_value=['formula1.rb', 'formula2.rb', 'not_a_formula.txt'])

    formulas = list(_get_formulas())
    
    assert formulas == ['formula1', 'formula2']

def test_get_formulas_exception(mock_get_brew_path_prefix, mocker):
    mock_get_brew_path_prefix.side_effect = Exception("Mocked exception")
    
    formulas = list(_get_formulas())
    
    assert formulas == []
