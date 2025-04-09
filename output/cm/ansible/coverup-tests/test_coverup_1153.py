# file lib/ansible/plugins/filter/mathstuff.py:54-88
# lines [59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 79, 80, 83, 84, 85, 86, 88]
# branches ['60->exit', '60->61', '66->67', '66->76', '76->79', '76->88', '79->80', '79->83', '84->85', '84->88', '85->84', '85->86']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import unique
from unittest.mock import MagicMock

# Mock the environment and the HAS_UNIQUE variable
@pytest.fixture
def mock_environment(mocker):
    environment = MagicMock()
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_UNIQUE', False)
    return environment

# Test function to cover lines 59-88
def test_unique_filter_with_case_insensitive_and_attribute(mock_environment, mocker):
    # Mock the do_unique function to raise a TypeError
    mocker.patch('ansible.plugins.filter.mathstuff.do_unique', side_effect=TypeError)

    # Test with case_sensitive=False and attribute set
    with pytest.raises(AnsibleFilterError) as excinfo:
        unique(mock_environment, ['a', 'A'], case_sensitive=False, attribute='test')
    assert "Ansible's unique filter does not support case_sensitive=False nor attribute parameters" in str(excinfo.value)

    # Test with attribute set and case_sensitive=None
    with pytest.raises(AnsibleFilterError) as excinfo:
        unique(mock_environment, ['a', 'A'], attribute='test')
    assert "Ansible's unique filter does not support case_sensitive=False nor attribute parameters" in str(excinfo.value)

    # Test with case_sensitive=False and no attribute
    with pytest.raises(AnsibleFilterError) as excinfo:
        unique(mock_environment, ['a', 'A'], case_sensitive=False)
    assert "Ansible's unique filter does not support case_sensitive=False nor attribute parameters" in str(excinfo.value)

    # Test with case_sensitive=None and no attribute to cover lines 83-86
    result = unique(mock_environment, ['a', 'A'])
    assert result == ['a', 'A'], "The unique filter did not return the expected list"
