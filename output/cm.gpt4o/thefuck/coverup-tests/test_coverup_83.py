# file thefuck/rules/brew_install.py:22-23
# lines [22, 23]
# branches []

import pytest
from thefuck.rules.brew_install import _get_similar_formula
from thefuck.utils import get_closest

@pytest.fixture
def mock_get_closest(mocker):
    return mocker.patch('thefuck.rules.brew_install.get_closest')

@pytest.fixture
def mock_get_formulas(mocker):
    return mocker.patch('thefuck.rules.brew_install._get_formulas')

def test_get_similar_formula(mock_get_closest, mock_get_formulas):
    formula_name = 'test_formula'
    mock_get_formulas.return_value = ['test_formula1', 'test_formula2', 'test_formula3']
    mock_get_closest.return_value = 'test_formula1'

    result = _get_similar_formula(formula_name)

    mock_get_formulas.assert_called_once()
    mock_get_closest.assert_called_once_with(formula_name, ['test_formula1', 'test_formula2', 'test_formula3'], cutoff=0.85)
    assert result == 'test_formula1'
