# file thefuck/rules/brew_install.py:22-23
# lines [23]
# branches []

import pytest
from thefuck.rules.brew_install import _get_similar_formula
from thefuck.types import Command
from unittest.mock import patch

@pytest.fixture
def mock_get_formulas(mocker):
    return mocker.patch('thefuck.rules.brew_install._get_formulas', return_value=['formula1', 'formula2'])

@pytest.fixture
def mock_get_closest(mocker):
    return mocker.patch('thefuck.rules.brew_install.get_closest', return_value='formula1')

def test_get_similar_formula(mock_get_formulas, mock_get_closest):
    formula_name = 'formul'
    result = _get_similar_formula(formula_name)
    mock_get_formulas.assert_called_once_with()
    mock_get_closest.assert_called_once_with(formula_name, ['formula1', 'formula2'], cutoff=0.85)
    assert result == 'formula1'
