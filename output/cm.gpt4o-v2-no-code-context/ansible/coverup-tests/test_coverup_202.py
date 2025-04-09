# file: lib/ansible/plugins/filter/core.py:183-199
# asked: {"lines": [183, 184, 185, 186, 187, 188, 191, 196, 197, 199], "branches": [[186, 187], [186, 188], [188, 191], [188, 196], [196, 197], [196, 199]]}
# gained: {"lines": [183, 184, 185, 186, 187, 188, 191, 196, 197, 199], "branches": [[186, 187], [186, 188], [188, 191], [188, 196], [196, 197], [196, 199]]}

import pytest
from ansible.plugins.filter.core import regex_escape, AnsibleFilterError
from ansible.module_utils._text import to_text
import re

def test_regex_escape_python():
    result = regex_escape("a.b*c")
    assert result == re.escape("a.b*c")

def test_regex_escape_posix_basic():
    result = regex_escape("a.b*c", re_type='posix_basic')
    assert result == r'a\.b\*c'

def test_regex_escape_posix_extended():
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape("a.b*c", re_type='posix_extended')
    assert str(excinfo.value) == 'Regex type (posix_extended) not yet implemented'

def test_regex_escape_invalid_type():
    with pytest.raises(AnsibleFilterError) as excinfo:
        regex_escape("a.b*c", re_type='invalid_type')
    assert str(excinfo.value) == 'Invalid regex type (invalid_type)'
