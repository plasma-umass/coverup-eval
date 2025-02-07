# file: lib/ansible/plugins/filter/mathstuff.py:54-88
# asked: {"lines": [54, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88], "branches": [[60, 0], [60, 61], [66, 67], [66, 76], [76, 79], [76, 88], [79, 80], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}
# gained: {"lines": [54, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 76, 79, 83, 84, 85, 86, 88], "branches": [[60, 61], [66, 67], [66, 76], [76, 79], [79, 83], [84, 85], [84, 88], [85, 84], [85, 86]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import unique

@pytest.fixture
def mock_environment():
    return MagicMock()

def test_unique_with_case_sensitive_false(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True), \
         patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError):
        with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
            unique(mock_environment, [1, 2, 2], case_sensitive=False)

def test_unique_with_attribute(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True), \
         patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError):
        with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
            unique(mock_environment, [{'a': 1}, {'a': 2}, {'a': 2}], attribute='a')

def test_unique_fallback_no_case_sensitive_no_attribute(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False):
        result = unique(mock_environment, [1, 2, 2])
        assert result == [1, 2]

def test_unique_fallback_with_error(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True), \
         patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=Exception):
        with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
            unique(mock_environment, [1, 2, 2], case_sensitive=False)

def test_unique_no_unique_support(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False):
        result = unique(mock_environment, [1, 2, 2])
        assert result == [1, 2]
