# file lib/ansible/module_utils/facts/collector.py:78-82
# lines [78, 79, 80, 81, 82]
# branches ['80->81', '80->82']

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockedCollector(BaseFactCollector):
    _platform = 'TestOS'

def test_platform_match_positive(mocker):
    platform_info = {'system': 'TestOS'}
    assert MockedCollector.platform_match(platform_info) is MockedCollector

def test_platform_match_negative(mocker):
    platform_info = {'system': 'OtherOS'}
    assert MockedCollector.platform_match(platform_info) is None

def test_platform_match_no_system_key(mocker):
    platform_info = {}
    assert MockedCollector.platform_match(platform_info) is None
