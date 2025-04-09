# file: lib/ansible/utils/color.py:73-93
# asked: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}
# gained: {"lines": [73, 76, 77, 78, 79, 90, 91, 93], "branches": [[76, 77], [76, 93], [79, 90], [79, 91]]}

import pytest
from ansible.utils.color import stringc
from ansible.utils.color import ANSIBLE_COLOR
from ansible.utils.color import parsecolor

@pytest.fixture
def mock_ansible_color_true(monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)

@pytest.fixture
def mock_ansible_color_false(monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', False)

def test_stringc_with_color(mock_ansible_color_true, mocker):
    mock_parsecolor = mocker.patch('ansible.utils.color.parsecolor', return_value='31')
    result = stringc('hello', 'red')
    assert result == '\033[31mhello\033[0m'
    mock_parsecolor.assert_called_once_with('red')

def test_stringc_without_color(mock_ansible_color_false):
    result = stringc('hello', 'red')
    assert result == 'hello'

def test_stringc_with_wrap_nonvisible_chars(mock_ansible_color_true, mocker):
    mock_parsecolor = mocker.patch('ansible.utils.color.parsecolor', return_value='31')
    result = stringc('hello', 'red', wrap_nonvisible_chars=True)
    assert result == '\001\033[31m\002hello\001\033[0m\002'
    mock_parsecolor.assert_called_once_with('red')

def test_stringc_multiline(mock_ansible_color_true, mocker):
    mock_parsecolor = mocker.patch('ansible.utils.color.parsecolor', return_value='31')
    result = stringc('hello\nworld', 'red')
    assert result == '\033[31mhello\033[0m\n\033[31mworld\033[0m'
    mock_parsecolor.assert_called_once_with('red')
