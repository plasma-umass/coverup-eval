# file lib/ansible/plugins/filter/mathstuff.py:140-149
# lines [142, 143, 145, 146, 148, 149]
# branches ['142->143', '142->145', '145->146', '145->148']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.mathstuff import max as max_filter

# Mocking the HAS_MIN_MAX constant
@pytest.fixture
def mock_has_min_max(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.HAS_MIN_MAX', False)

# Test function to cover lines 142-149
def test_max_without_has_min_max(mock_has_min_max):
    # Test with no kwargs, should use the built-in max
    assert max_filter(None, [1, 2, 3]) == 3

    # Test with kwargs, should raise AnsibleFilterError
    with pytest.raises(AnsibleFilterError) as excinfo:
        max_filter(None, [1, 2, 3], some_kwarg=True)
    assert "Ansible's max filter does not support any keyword arguments." in str(excinfo.value)
