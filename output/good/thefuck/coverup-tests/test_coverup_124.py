# file thefuck/rules/brew_install.py:9-19
# lines []
# branches ['16->15']

import os
import pytest
from thefuck.rules.brew_install import _get_formulas
from unittest.mock import patch, mock_open

def test__get_formulas_with_rb_files(mocker):
    mocker.patch('thefuck.rules.brew_install.get_brew_path_prefix', return_value='/usr/local')
    mocker.patch('os.listdir', return_value=['package.rb', 'another_package.rb', 'not_a_formula.txt'])

    formulas = list(_get_formulas())

    assert 'package' in formulas
    assert 'another_package' in formulas
    assert 'not_a_formula' not in formulas

def test__get_formulas_without_rb_files(mocker):
    mocker.patch('thefuck.rules.brew_install.get_brew_path_prefix', return_value='/usr/local')
    mocker.patch('os.listdir', return_value=['not_a_formula.txt'])

    formulas = list(_get_formulas())

    assert not formulas
