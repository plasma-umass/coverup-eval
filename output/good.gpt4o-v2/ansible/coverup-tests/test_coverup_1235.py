# file: lib/ansible/plugins/filter/mathstuff.py:54-88
# asked: {"lines": [74, 80], "branches": [[60, 0], [76, 88], [79, 80]]}
# gained: {"lines": [74, 80], "branches": [[60, 0], [79, 80]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import unique

@pytest.fixture
def mock_environment():
    return MagicMock()

def test_unique_case_sensitive_false(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True):
        with patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError):
            with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
                unique(mock_environment, [1, 2, 2], case_sensitive=False)

def test_unique_attribute(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True):
        with patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError):
            with pytest.raises(AnsibleFilterError, match="Jinja2's unique filter failed and we cannot fall back to Ansible's version"):
                unique(mock_environment, [{'a': 1}, {'a': 2}, {'a': 2}], attribute='a')

def test_unique_fallback_warning(mock_environment, caplog):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', True):
        with patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=Exception):
            with patch('ansible.plugins.filter.mathstuff.display') as mock_display:
                result = unique(mock_environment, [1, 2, 2])
                assert result == [1, 2]
                mock_display.warning.assert_called_once()
                assert 'Falling back to Ansible unique filter as Jinja2 one failed:' in mock_display.warning.call_args[0][0]

def test_unique_no_unique_support(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False):
        result = unique(mock_environment, [1, 2, 2])
        assert result == [1, 2]

def test_unique_no_unique_support_case_sensitive_false(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False):
        with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
            unique(mock_environment, [1, 2, 2], case_sensitive=False)

def test_unique_no_unique_support_attribute(mock_environment):
    with patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False):
        with pytest.raises(AnsibleFilterError, match="Ansible's unique filter does not support case_sensitive=False nor attribute parameters"):
            unique(mock_environment, [{'a': 1}, {'a': 2}, {'a': 2}], attribute='a')
