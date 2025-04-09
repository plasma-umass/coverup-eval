# file: lib/ansible/utils/color.py:96-101
# asked: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}
# gained: {"lines": [96, 98, 99, 100, 101], "branches": [[99, 100], [99, 101]]}

import pytest
from ansible.utils.color import colorize, ANSIBLE_COLOR, stringc

@pytest.fixture
def setup_ansible_color(monkeypatch):
    original_ansible_color = ANSIBLE_COLOR
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    yield
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', original_ansible_color)

def test_colorize_no_color():
    result = colorize('test', 0, None)
    assert result == 'test=0   '

def test_colorize_with_color(setup_ansible_color, mocker):
    mock_stringc = mocker.patch('ansible.utils.color.stringc', return_value='colored_string')
    result = colorize('test', 1, 'red')
    mock_stringc.assert_called_once_with('test=1   ', 'red')
    assert result == 'colored_string'
