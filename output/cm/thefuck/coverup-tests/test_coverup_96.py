# file thefuck/rules/choco_install.py:4-7
# lines [4, 5, 6, 7]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.choco_install import match

@pytest.fixture
def choco_install_command():
    return Command('choco install somepackage', 'Installing the following packages')

@pytest.fixture
def cinst_command():
    return Command('cinst somepackage', 'Installing the following packages')

@pytest.fixture
def non_choco_command():
    return Command('echo choco install somepackage', '')

@pytest.fixture
def choco_install_no_output_command():
    return Command('choco install somepackage', '')

def test_match_with_choco_install(choco_install_command):
    assert match(choco_install_command)

def test_match_with_cinst(cinst_command):
    assert match(cinst_command)

def test_not_match_with_non_choco_command(non_choco_command):
    assert not match(non_choco_command)

def test_not_match_with_choco_install_no_output(choco_install_no_output_command):
    assert not match(choco_install_no_output_command)
