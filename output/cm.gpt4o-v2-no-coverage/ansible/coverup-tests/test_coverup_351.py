# file: lib/ansible/executor/interpreter_discovery.py:165-178
# asked: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}
# gained: {"lines": [165, 166, 168, 169, 171, 173, 174, 176, 178], "branches": [[168, 169], [168, 171], [173, 174], [173, 176]]}

import pytest
from ansible.executor.interpreter_discovery import _get_linux_distro
from ansible.module_utils.distro import LinuxDistribution
from unittest.mock import patch, mock_open

@pytest.fixture
def platform_info_with_dist_result():
    return {
        'platform_dist_result': ['Ubuntu', '20.04', 'focal']
    }

@pytest.fixture
def platform_info_with_osrelease_content():
    return {
        'osrelease_content': 'NAME="Ubuntu"\nVERSION="20.04.1 LTS (Focal Fossa)"\nID=ubuntu\nVERSION_ID="20.04"\n'
    }

@pytest.fixture
def platform_info_empty():
    return {}

def test_get_linux_distro_with_dist_result(platform_info_with_dist_result):
    result = _get_linux_distro(platform_info_with_dist_result)
    assert result == ('Ubuntu', '20.04')

def test_get_linux_distro_with_osrelease_content(platform_info_with_osrelease_content):
    with patch('builtins.open', mock_open(read_data=platform_info_with_osrelease_content['osrelease_content'])):
        result = _get_linux_distro(platform_info_with_osrelease_content)
        assert result == ('ubuntu', '20.04')

def test_get_linux_distro_empty(platform_info_empty):
    result = _get_linux_distro(platform_info_empty)
    assert result == (u'', u'')
