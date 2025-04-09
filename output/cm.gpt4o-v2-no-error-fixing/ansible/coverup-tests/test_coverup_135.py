# file: lib/ansible/plugins/filter/core.py:183-199
# asked: {"lines": [183, 184, 185, 186, 187, 188, 191, 196, 197, 199], "branches": [[186, 187], [186, 188], [188, 191], [188, 196], [196, 197], [196, 199]]}
# gained: {"lines": [183, 184, 185, 186, 187, 188, 191, 196, 197, 199], "branches": [[186, 187], [186, 188], [188, 191], [188, 196], [196, 197], [196, 199]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import regex_escape

def test_regex_escape_python():
    assert regex_escape("a.b*c") == r"a\.b\*c"

def test_regex_escape_posix_basic(mocker):
    mocker.patch('ansible.plugins.filter.core.regex_replace', return_value=r'a\.b\*c')
    assert regex_escape("a.b*c", re_type='posix_basic') == r'a\.b\*c'

def test_regex_escape_posix_extended():
    with pytest.raises(AnsibleFilterError, match=r"Regex type \(posix_extended\) not yet implemented"):
        regex_escape("a.b*c", re_type='posix_extended')

def test_regex_escape_invalid_type():
    with pytest.raises(AnsibleFilterError, match=r"Invalid regex type \(invalid_type\)"):
        regex_escape("a.b*c", re_type='invalid_type')
