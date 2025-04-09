# file lib/ansible/modules/pip.py:310-312
# lines [310, 312]
# branches []

import pytest
from ansible.modules.pip import _is_package_name

@pytest.fixture
def op_dict(mocker):
    mock_op_dict = mocker.patch('ansible.modules.pip.op_dict')
    mock_op_dict.keys.return_value = ['==', '>=', '<=', '>', '<', '!=']
    return mock_op_dict

def test_is_package_name_with_package_name(op_dict):
    assert _is_package_name("requests") is True

def test_is_package_name_with_version_specifier(op_dict):
    # The test case is incorrect because "requests>=2.0" starts with a package name, not a version specifier.
    # The correct test case should only have the version specifier without a package name.
    assert _is_package_name(">=2.0") is False

def test_is_package_name_with_leading_space_and_package_name(op_dict):
    assert _is_package_name("  requests") is True

def test_is_package_name_with_leading_space_and_version_specifier(op_dict):
    assert _is_package_name("  >=2.0") is False
