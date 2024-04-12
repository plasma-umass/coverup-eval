# file lib/ansible/plugins/filter/core.py:183-199
# lines [183, 184, 185, 186, 187, 188, 191, 196, 197, 199]
# branches ['186->187', '186->188', '188->191', '188->196', '196->197', '196->199']

import pytest
import re
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import regex_escape

def test_regex_escape_python_type(mocker):
    mocker.patch('ansible.plugins.filter.core.to_text', return_value='test_string')
    result = regex_escape('test_string', re_type='python')
    assert result == re.escape('test_string')

def test_regex_escape_posix_basic_type(mocker):
    mocker.patch('ansible.plugins.filter.core.to_text', return_value='test.string')
    mocker.patch('ansible.plugins.filter.core.regex_replace', return_value='test\\.string')
    result = regex_escape('test.string', re_type='posix_basic')
    assert result == 'test\\.string'

def test_regex_escape_invalid_type(mocker):
    mocker.patch('ansible.plugins.filter.core.to_text', return_value='test_string')
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape('test_string', re_type='invalid')
    assert 'Invalid regex type (invalid)' in str(excinfo.value)

def test_regex_escape_posix_extended_type(mocker):
    mocker.patch('ansible.plugins.filter.core.to_text', return_value='test_string')
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape('test_string', re_type='posix_extended')
    assert 'Regex type (posix_extended) not yet implemented' in str(excinfo.value)
