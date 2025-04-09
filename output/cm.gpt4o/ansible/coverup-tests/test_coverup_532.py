# file lib/ansible/utils/color.py:96-101
# lines [96, 98, 99, 100, 101]
# branches ['99->100', '99->101']

import pytest
from ansible.utils.color import colorize
from ansible.utils.color import ANSIBLE_COLOR
from ansible.utils.color import stringc

@pytest.fixture
def mock_ansible_color(mocker):
    original_value = ANSIBLE_COLOR
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', True)
    yield
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', original_value)

def test_colorize_no_color(mock_ansible_color):
    result = colorize('test', 0, None)
    assert result == 'test=0   '

def test_colorize_with_color(mock_ansible_color, mocker):
    mock_stringc = mocker.patch('ansible.utils.color.stringc', return_value='colored_string')
    result = colorize('test', 1, 'red')
    mock_stringc.assert_called_once_with('test=1   ', 'red')
    assert result == 'colored_string'
