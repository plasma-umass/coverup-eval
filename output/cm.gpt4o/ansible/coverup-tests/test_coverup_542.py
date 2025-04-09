# file lib/ansible/module_utils/facts/collector.py:78-82
# lines [78, 79, 80, 81, 82]
# branches ['80->81', '80->82']

import pytest
from unittest.mock import patch

# Assuming the BaseFactCollector class is defined in ansible.module_utils.facts.collector
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector(BaseFactCollector):
    _platform = 'Linux'

@pytest.fixture
def platform_info():
    return {'system': 'Linux'}

def test_platform_match(platform_info):
    assert TestBaseFactCollector.platform_match(platform_info) == TestBaseFactCollector

def test_platform_no_match():
    platform_info = {'system': 'Windows'}
    assert TestBaseFactCollector.platform_match(platform_info) is None
