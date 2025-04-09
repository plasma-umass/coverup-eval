# file lib/ansible/utils/color.py:104-112
# lines [104, 105, 106, 107, 108, 109, 111, 112]
# branches ['105->106', '105->112', '106->107', '106->108', '108->109', '108->111']

import pytest
from ansible.utils.color import hostcolor, stringc, C
from unittest.mock import patch

# Mocking the ANSIBLE_COLOR constant to ensure it is True for the test
@pytest.fixture
def mock_ansible_color_true(mocker):
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', True)

# Mocking the ANSIBLE_COLOR constant to ensure it is False for the test
@pytest.fixture
def mock_ansible_color_false(mocker):
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', False)

# Test function to cover the branches where stats indicate failures or unreachable hosts
@pytest.mark.usefixtures("mock_ansible_color_true")
def test_hostcolor_with_failures_or_unreachable():
    stats_failure = {'failures': 1, 'unreachable': 0, 'changed': 0}
    stats_unreachable = {'failures': 0, 'unreachable': 1, 'changed': 0}
    host = 'test_host'
    assert hostcolor(host, stats_failure) == u"%-37s" % stringc(host, C.COLOR_ERROR)
    assert hostcolor(host, stats_unreachable) == u"%-37s" % stringc(host, C.COLOR_ERROR)

# Test function to cover the branch where stats indicate changed hosts
@pytest.mark.usefixtures("mock_ansible_color_true")
def test_hostcolor_with_changes():
    stats_changed = {'failures': 0, 'unreachable': 0, 'changed': 1}
    host = 'test_host'
    assert hostcolor(host, stats_changed) == u"%-37s" % stringc(host, C.COLOR_CHANGED)

# Test function to cover the branch where stats indicate no changes, failures, or unreachable hosts
@pytest.mark.usefixtures("mock_ansible_color_true")
def test_hostcolor_with_no_changes_failures_unreachable():
    stats_ok = {'failures': 0, 'unreachable': 0, 'changed': 0}
    host = 'test_host'
    assert hostcolor(host, stats_ok) == u"%-37s" % stringc(host, C.COLOR_OK)

# Test function to cover the branch where ANSIBLE_COLOR is False
@pytest.mark.usefixtures("mock_ansible_color_false")
def test_hostcolor_without_color():
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    host = 'test_host'
    assert hostcolor(host, stats, color=False) == u"%-26s" % host
